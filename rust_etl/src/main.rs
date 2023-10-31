use std::env;

mod extract;
mod transform_load;
mod query;

pub fn main() {
    match std::env::args().nth(1).as_deref() {
        Some("extract") => { extract::run().expect("Failed to run extract"); },
        Some("transform_load") => { transform_load::main().expect("Failed to run transform_load"); },
        Some("query") => { query::query().expect("Failed to run query"); },
        _ => println!("Invalid command provided"),
    };
}