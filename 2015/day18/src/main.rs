use std::io::prelude::*;
use ndarray::Array2;

const SIZE : usize = 100;

fn run(grid : &mut Array2<usize>, stuck : u32) -> Array2<usize> {
    use itertools::Itertools;
    use std::cmp;

    let mut new_grid = Array2::<usize>::zeros((SIZE, SIZE));
    for x in 0i32..SIZE as i32 {
        for y in 0i32..SIZE as i32 {
            let left = cmp::max(0, x-1);
            let right = cmp::min(SIZE - 1, x as usize+1);
            let bottom = cmp::max(0, y-1);
            let top = cmp::min(SIZE - 1, y as usize+1);
            let mut sum = 0;
            let mut is_on = 0;

            let range = (left as usize..=right as usize).cartesian_product(bottom as usize..=top as usize);
            for loc in range {
                let spot = grid.get_mut(loc).unwrap();
                if loc == (x as usize, y as usize) {
                    is_on = *spot;
                } else if *spot == 1 {
                    sum += 1;
                }
            }

            let spot = new_grid.get_mut((x as usize, y as usize)).unwrap();
            if stuck == 1 && (x == 0 || x == SIZE as i32 - 1) && (y == 0 || y == SIZE as i32 - 1) {
                *spot = 1;
            } else if is_on == 1 && (sum == 2 || sum == 3) {
                *spot = 1;
            } else if is_on == 0 && sum == 3 {
                *spot = 1;
            } else {
                *spot = 0;
            }
        }
    }

    new_grid
}

fn main() -> std::io::Result<()> {
    use std::fs::File;
    use std::io::BufReader;

    let file = File::open("18")?;

    let mut grid = Array2::<usize>::zeros((SIZE, SIZE));
    let reader = BufReader::new(file);
    for (x, line) in reader.lines().enumerate() {
        for (y, ch) in line.unwrap().chars().enumerate() {
            let spot = grid.get_mut((x, y)).unwrap();
            *spot = match ch {
                '#' => 1,
                _ => 0
            };
        }
    }
    let o_grid = grid.clone();

    for _c in 0..100 {
        grid = run(&mut grid, 0);
    }
    println!("Part 1: {}", grid.sum());

    grid = o_grid;
    for _c in 0..100 {
        grid = run(&mut grid, 1);
    }
    println!("Part 2: {}", grid.sum());

    Ok(())
}
