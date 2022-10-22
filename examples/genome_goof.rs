use std::time::Instant;

use icpc_stuff::goof::{recursive_goof, goof};

fn test_string_goof<S: AsRef<str>>(s: S) -> usize {
    let chars: Vec<char> = s.as_ref().chars().collect();
    let len = goof(&chars);
    len
}


fn main() {
    let start = Instant::now();
    let len = test_string_goof("ATTT");
    println!("Goof return a lenth of {len} in {:?}", start.elapsed());

    let start = Instant::now();
    let len = test_string_goof("ATTACC");
    println!("Goof return a lenth of {len} in {:?}", start.elapsed());

    let start = Instant::now();
    let len = test_string_goof("AAAAGAATTAA");
    println!("Goof return a lenth of {len} in {:?}", start.elapsed());
}