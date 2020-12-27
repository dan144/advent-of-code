fn main() {
    let min = 29000000;

    println!("Minimum presents: {:?}", min);

    let mut house = 1;
    while min > 10 * (1..house).into_iter().filter(|i| house % i == 0).sum::<i64>() {
        house += 1;
    }
    println!("Part 1: {:?}", house);

    let mut houses = vec![0; min as usize / 10];
    let mut m_h = 0;
    for elf in 1..=houses.len() {
        for j in (1..=50).into_iter() {
            let house = (j*elf) - 1;
            if house >= houses.len() {
                continue;
            }
            houses[house] += elf * 11;
            if houses[house] >= min as usize {
                if m_h == 0 || m_h > house {
                    println!("Part 2: {:?} {:?} {:?}", house+1, houses[house], elf);
                    m_h = house+1;
                }
            }
        }
    }
}
