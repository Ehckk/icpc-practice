use std::time::Instant;

use icpc_stuff::goof::{recursive_goof, goof};

fn test_string_goof<S: AsRef<str>>(s: S) -> usize {
    let chars: Vec<char> = s.as_ref().chars().collect();
    let len = goof(&chars);
    len
}

fn test_string_goof_recursive<S: AsRef<str>>(s: S) -> usize {
    let chars: Vec<char> = s.as_ref().chars().collect();
    let len = recursive_goof(&chars);
    len
}

fn test_str<S: AsRef<str>>(s: S) {
    let s = s.as_ref();
    println!("Testing {:?}", s);
    // Do it non-recursively
    let start = Instant::now();
    let count = test_string_goof(s);
    println!("{:?} in order to get {count}", start.elapsed());
    // Do it recursively
    let start = Instant::now();
    let count = test_string_goof_recursive(s);
    println!("{:?} in order to get {count} recursively", start.elapsed());
}

fn main() {
    test_str("AAAATTAAAAAAAGGGCCGG");
    test_str("ATTACC");
    test_str("AAAAGAATTAA");
}