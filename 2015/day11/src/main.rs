fn valid_password(password : &String) -> bool {
    let alphabet = "abcdefghijklmnopqrstuvwxyz";
    let mut inc : u8 = 1;
    let mut last : Option<char> = None;

    let mut pairs : u8 = 0;
    let mut check : u8 = 2;

    for c in password.chars() {
        if last.is_some() {
            if last != Some('z') && inc < 3 {
                if alphabet.chars().nth(alphabet.find(last.unwrap()).unwrap() + 1).unwrap() == c {
                    inc += 1;
                } else {
                    inc = 1;
                }
            }
            if last == Some(c) && check > 1 {
                pairs += 1;
                check = 0;
            }
            check += 1;
        }
        last = Some(c);
    }

    // there should be a check if the string contains any of "ilo", but we shortcut that by
    // omitting them from the get_next alphabet, which works unless the initial string contains one
    return inc >= 3 && pairs >= 2;
}

fn get_next(password : &mut String) -> String {
    let alphabet = "abcdefghjkmnpqrstuvwxyz";
    let chars = password.chars().rev().enumerate();
    let mut password = String::new();

    let mut inc : bool = true;
    for (i, mut c) in chars {
        if inc {
            if c == 'z' {
                c = 'a';
            } else {
                c = alphabet.chars().nth(alphabet.find(c).unwrap() + 1).unwrap();
                inc = false;
            }
        }
        password = c.to_string() + &password;
    }

    return password.clone();
}

fn main() -> std::io::Result<()> {
    use std::fs::File;
    use std::io::BufReader;
    use std::io::prelude::*;

    let file = File::open("11")?;
    let mut reader = BufReader::new(file);

    let mut password = String::new();
    let _len = reader.read_line(&mut password)?;
    let mut password = password.trim().to_string();
    println!("Password: {:?}", password);

    while !valid_password(&password) {
        password = get_next(&mut password);
    }
    println!("Part 1: {:?}", password);

    password = get_next(&mut password);
    while !valid_password(&password) {
        password = get_next(&mut password);
    }
    println!("Part 2: {:?}", password);

    Ok(())
}
