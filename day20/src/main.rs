fn main() {
    use factor::factor_include::factor_include;
    let min = 29000000;
    println!("Minimum presents: {:?}", 10 * min);

    let mut house = 1;
    while min > 10 * (1..house).into_iter().filter(|i| house % i == 0).sum::<i64>() {
        house += 1;
    }
    println!("Part 1: {:?}", house);
}
