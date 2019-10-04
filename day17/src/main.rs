fn main() -> std::io::Result<()> {
    use std::fs::File;
    use std::io::BufReader;
    use std::io::prelude::*;
    use itertools::Itertools;

    let file = File::open("17")?;
    let mut reader = BufReader::new(file);
    let mut line = String::new();

    let mut buckets = Vec::new();

    while let Ok(n) = reader.read_line(&mut line) {
        if n == 0 {
            break;
        }
        let sz = line.trim().parse::<i32>().unwrap();
        buckets.push(sz);
        line.clear();
    };

    let eggnog = 150;  // input
    let mut works = 0;
    for l in 0..buckets.len() {
        let it = buckets.iter().combinations(l);
        for p in it {
            let mut total = eggnog;
            for x in 0..p.len() {
                total -= p[x];
            }
            if total == 0 {
                works += 1;
            }
        }
    }

    println!("Part 1: {:?}", works);
    // println!("Part 2: {:?}", reduce(map.clone()));

    Ok(())
}
