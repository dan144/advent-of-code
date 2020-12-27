use permutohedron::Heap;
use regex::Regex;
use std::collections::HashMap;

fn reduce(map : HashMap <String, HashMap<String, i32>>) -> i32 {
    let mut name_vec = map.keys().cloned().collect::<Vec<String>>();
    let heap = Heap::new(&mut name_vec);
    let mut max : i32 = 0;
    for p in heap {
        let mut total : i32 = 0;
        for x in 0..p.len() {
            let prev_idx = x.checked_sub(1).unwrap_or(p.len() - 1);
            let x_p = *map.get(&p[x]).unwrap().get(&p[prev_idx]).unwrap();
            let p_x = *map.get(&p[prev_idx]).unwrap().get(&p[x]).unwrap();
            total += x_p + p_x;
        }
        if total > max {
            max = total;
        }
    }
    max
}

fn main() -> std::io::Result<()> {
    use std::fs::File;
    use std::io::BufReader;
    use std::io::prelude::*;

    let file = File::open("13")?;
    let mut reader = BufReader::new(file);
    let mut line = String::new();

    let mut map : HashMap <String, HashMap<String, i32>> = HashMap::new();

    while let Ok(n) = reader.read_line(&mut line) {
        if n == 0 {
            break;
        }
        let re = Regex::new(r"(?P<person>\w+) would (?P<action>\w{4}) (?P<number>\d+) happiness units by sitting next to (?P<cause>\w+).").unwrap();
        let caps = re.captures(&line).unwrap();
        let person = &caps["person"];
        let cause = &caps["cause"];
        let value : i32 = &caps["number"].parse().unwrap() * match &caps["action"] {
            "lose" => -1,
            _ => 1 // Some("gain")
        };
        map.entry(person.to_string()).or_insert(Default::default()).insert(cause.to_string(), value);
        line.clear();
    };
    println!("Part 1: {:?}", reduce(map.clone()));

    let name_vec = map.keys().cloned().collect::<Vec<String>>();
    map.entry("Daniel".to_string()).or_insert(Default::default());
    for name in name_vec {
        map.entry(name.to_string()).or_insert(Default::default()).insert("Daniel".to_string(), 0);
        map.entry("Daniel".to_string()).or_insert(Default::default()).insert(name.to_string(), 0);
    }
    println!("Part 2: {:?}", reduce(map.clone()));

    Ok(())
}
