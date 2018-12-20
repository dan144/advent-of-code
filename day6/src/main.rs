use regex::Regex;

type Coord = (usize, usize);

struct Rectangle {
    tl: Coord,
    br: Coord,
}

enum Action {
    TurnOn(Rectangle),
    TurnOff(Rectangle),
    Toggle(Rectangle),
}

// sample in
// turn on 489,959 through 759,964

use std::io::prelude::*;
use ndarray::Array2;

fn run(grid : &mut Array2<usize>, action : &Action) {
    use itertools::Itertools;
    let rect = match action {
        Action::TurnOn(rect) => rect,
        Action::TurnOff(rect) => rect,
        Action::Toggle(rect) => rect,
    };
    let range = (rect.tl.0..=rect.br.0).cartesian_product(rect.tl.1..=rect.br.1);
    for loc in range {
        let mut spot = grid.get_mut(loc).unwrap();
        match action {
            Action::TurnOn(_) => *spot = 1,
            Action::TurnOff(_) => *spot = 0,
            Action::Toggle(_) => *spot += 1,
        }
        *spot %= 2;
    }
}

fn main() -> std::io::Result<()> {
    use std::fs::File;
    let mut file = File::open("6")?;
    let mut buf = String::new();
    file.read_to_string(&mut buf)?;

    let re = Regex::new(r"(?P<action>turn off|turn on|toggle) (?P<tl>\d+,\d+) through (?P<br>\d+,\d+)").unwrap();
    let actions : Vec<Action> = buf.lines().map(| ln | {
        let caps = re.captures(ln).unwrap();
        let tl : Vec<usize> = caps["tl"].split(",").map(| i | i.parse::<usize>().unwrap()).collect();
        let tl : Coord = (tl[0], tl[1]);
        let br : Vec<usize> = caps["br"].split(",").map(| i | i.parse::<usize>().unwrap()).collect();
        let br : Coord = (br[0], br[1]);
        let rect = Rectangle{tl: tl, br: br};
        match &caps["action"] {
            "turn on" => Action::TurnOn(rect),
            "turn off" => Action::TurnOff(rect),
            "toggle" => Action::Toggle(rect),
            _ => unreachable!(),
        }
    }).collect();

    assert_eq!(buf.lines().count(), actions.len());

    let mut grid = Array2::<usize>::zeros((1000, 1000));

    for a in actions.iter() {
        run(&mut grid, a);
    }

    println!("{}", grid.sum());

    Ok(())
}
