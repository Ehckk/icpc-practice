use std::time::Instant;

use icpc_stuff::goof::{recursive_goof, goof};

fn test_str<S: AsRef<str>>(s: S) {
    let s = s.as_ref();
    println!("Testing {:?}", s);
    let chars: Vec<char> = s.chars().collect();
    // Do it non-recursively
    let start = Instant::now();
    let count = goof(&chars);
    println!("{:?} in order to get {count}", start.elapsed());
    // Do it recursively
    let start = Instant::now();
    let count = recursive_goof(&chars);
    println!("{:?} in order to get {count} recursively", start.elapsed());
}

fn main() {
    test_str("AAAATTAAAAAAAGGGCCGG");
    test_str("ATTACC");
    test_str("AAAAGAATTAA");
}