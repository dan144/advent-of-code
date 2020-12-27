#[macro_use]
extern crate nom;

use nom::{alpha,alphanumeric,digit};
use nom::types::CompleteStr;
use std::collections::HashMap;

named!(output_parser<CompleteStr, CompleteStr>,
    do_parse!(
        tag!(" -> ") >>
        output:alpha >>
        (output)
    )
);

#[derive(Debug, PartialEq)]
enum Operation {
    OperAnd(String, String),
    OperLShift(String, usize),
    OperNot(String),
    OperOr(String, String),
    OperRShift(String, usize),
    OperAssign(String),
    Value(u32),
}

named!(and_parser<CompleteStr, Operation>,
    do_parse!(
        left:alphanumeric >>
        tag!(" AND ") >>
        right:alphanumeric >>
        (Operation::OperAnd(left.as_ref().into(), right.as_ref().into()))
    )
);

named!(or_parser<CompleteStr, Operation>,
    do_parse!(
        left:alphanumeric >>
        tag!(" OR ") >>
        right:alphanumeric >>
        (Operation::OperOr(left.as_ref().into(), right.as_ref().into()))
    )
);

named!(lshift_parser<CompleteStr, Operation>,
    do_parse!(
        input:alpha >>
        tag!(" LSHIFT ") >>
        offset:digit >>
        (Operation::OperLShift(input.as_ref().into(), offset.parse().unwrap()))
    )
);

named!(rshift_parser<CompleteStr, Operation>,
    do_parse!(
        input:alpha >>
        tag!(" RSHIFT ") >>
        offset:digit >>
    (Operation::OperRShift(input.as_ref().into(), offset.parse().unwrap())))
);

named!(not_parser<CompleteStr, Operation>,
    do_parse!(
        tag!("NOT ") >>
        input:alpha >>
    (Operation::OperNot(input.as_ref().into())))
);

named!(value_parser<CompleteStr, Operation>,
    do_parse!(
        input:digit >>
    (Operation::Value(input.parse().unwrap())))
);

named!(assign_parser<CompleteStr, Operation>,
    do_parse!(
        input:alpha >>
    (Operation::OperAssign(input.parse().unwrap())))
);

named!(operation_parser<CompleteStr, (Operation, String)>,
    do_parse!(
        capture:alt!(
            and_parser|
            or_parser|
            lshift_parser|
            rshift_parser|
            not_parser|
            value_parser|
            assign_parser) >>
        output:output_parser >>
        ((capture, output.as_ref().into()))
    )
);

fn reduce(operations : &mut HashMap<String, Operation>) -> bool {
    let mut changed : i32 = 0;
    let mut values : HashMap<String, Operation> = HashMap::new();
    // operations.iter().filter_map(| (output, operation) | {
    //     match operation {
    //         Operation::Value (x) => Some((output, x)),
    //         _ => None
    //     }
    // }).collect();

    for (output, operation) in operations.iter_mut() {
        match operation {
            Operation::Value (v) => {
                values.insert(output.to_string(), Operation::Value(*v));
                changed += 1;
            }
            Operation::OperAnd (l, r) => {
                let result = l.parse::<u32>().and_then( | l_i | r.parse::<u32>().and_then( | r_i | {
                    Ok(Operation::Value(l_i & r_i))
                }));
                if let Ok(result) = result {
                    values.insert(output.to_string(), result);
                    changed += 1;
                }
            }
            Operation::OperOr (l, r) => {
                let result = l.parse::<u32>().and_then( | l_i | r.parse::<u32>().and_then( | r_i | {
                    Ok(Operation::Value(l_i | r_i))
                }));
                if let Ok(result) = result {
                    values.insert(output.to_string(), result);
                    changed += 1;
                }
            }
            Operation::OperLShift (v, n) => {
                let result = v.parse::<u32>().and_then( | v_i | {
                    Ok(Operation::Value(v_i << *n))
                });
                if let Ok(result) = result {
                    values.insert(output.to_string(), result);
                    changed += 1;
                }
            }
            Operation::OperRShift (v, n) => {
                let result = v.parse::<u32>().and_then( | v_i | {
                    Ok(Operation::Value(v_i >> *n))
                });
                if let Ok(result) = result {
                    values.insert(output.to_string(), result);
                    changed += 1;
                }
            }
            Operation::OperNot (v) => {
                let result = v.parse::<u32>().and_then( | v_i | {
                    Ok(Operation::Value(!v_i))
                });
                if let Ok(result) = result {
                    values.insert(output.to_string(), result);
                    changed += 1;
                }
            }
            Operation::OperAssign (v) => {
                let result = v.parse::<u32>().and_then( | v_i | {
                    Ok(Operation::Value(v_i))
                });
                if let Ok(result) = result {
                    values.insert(output.to_string(), result);
                    changed += 1;
                }
            }
        }
    }

    println!("{:?}", values.len());
    for (output, value) in values.drain() {
        // operations.entry(output.clone()).and_modify( | operation | match operation {
        for (o_output, operation) in operations.iter_mut() {
            match operation {
                Operation::Value (_) => {}
                Operation::OperAnd (l, r) => {
                    if let Operation::Value(value) = value {
                        if *l == output {
                            *l = value.to_string();
                        }
                        if *r == output {
                            *r = value.to_string();
                        }
                    }
                }
                Operation::OperOr (l, r) => {
                    if let Operation::Value(value) = value {
                        if *l == output {
                            *l = value.to_string();
                        }
                        if *r == output {
                            *r = value.to_string();
                        }
                    }
                }
                Operation::OperLShift (v, n) => {
                    if let Operation::Value(value) = value {
                        if *v == output {
                            *v = value.to_string();
                        }
                    }
                }
                Operation::OperRShift (v, n) => {
                    if let Operation::Value(value) = value {
                        if *v == output {
                            *v = value.to_string();
                        }
                    }
                }
                Operation::OperNot (v) => {
                    if let Operation::Value(value) = value {
                        if *v == output {
                            *v = value.to_string();
                        }
                    }
                }
                Operation::OperAssign (v) => {
                    if let Operation::Value(value) = value {
                        if *v == output {
                            *v = value.to_string();
                        }
                    }
                }
            }
        }
    }

    println!("Value of A: {:?}", operations["a"]);
    return match changed {
        0 => false,
        _ => true
    }
}

fn main() -> std::io::Result<()> {
    use std::fs::File;
    use std::io::prelude::*;

    let mut file = File::open("7")?;
    let mut buf = String::new();
    file.read_to_string(&mut buf)?;

    let mut operations : HashMap<String, Operation> = buf.lines().map(| ln | {
        operation_parser(ln.into()).unwrap().1
    }).map(| (x, y) | (y, x)).collect();

    while reduce(&mut operations){};
    println!("Value of A: {:?}", operations["a"]);

    Ok(())
}

#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn parse_and() {
        let input = "eg AND ei -> ej";
        let exp_op = Operation::OperAnd("eg".into(), "ei".into());
        assert_eq!(exp_op, and_parser(input.into()).unwrap().1);
        assert_eq!((exp_op, "ej".into()), operation_parser(input.into()).unwrap().1);
    }
}
