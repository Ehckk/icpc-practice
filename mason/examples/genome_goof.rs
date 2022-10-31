use std::time::Instant;

use icpc_stuff::{goof::{recursive_goof, goof, goof_ff}, comb::Combinations};

fn test_str<S: AsRef<str>>(s: S) {
    let s = s.as_ref();
    let chars: Vec<char> = s.chars().collect();
    if s.len() < 100 {
        println!("Testing {:?}", s);
    }
    else {
        println!("Testing sequence of length {:?}", s.len());
    }
    // Fold at first chance
    let start = Instant::now();
    let count = goof_ff(&chars);
    println!("{:?} in order to get {count} folding first", start.elapsed());
    // Do it non-recursively
    let start = Instant::now();
    let count = goof(&chars);
    println!("{:?} in order to get {count}", start.elapsed());
    
}

fn main() {
    // test_str("AAAATTAAAAAAAGGGCCGG");
    // test_str("ATTACC");
    // test_str("AAAAGAATTAA");
    // let mut longest_str = String::new();
    // for _ in 0..(4*10u64.pow(6)) {
    //     longest_str.push('A');
    // }
    // test_str(longest_str);
    for n in 0..20 {
        let combs = Combinations::from_choices(vec!['A','T','C','G'], n);
        let total_combs = combs.num_combs;
        let mut longest = Instant::now().elapsed();
        for comb in combs {
            let start = Instant::now();
            goof_ff(&comb);
            let diff = start.elapsed();
            if diff > longest {
                longest = diff;
            }
        }
        println!("The combinations of length {n} that took the longest took: {:?}", longest);
    }
    
}