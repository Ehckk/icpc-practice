use icpc_stuff::towering::solution;

use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let line = stdin.lock()
		.lines()
		.map(|l| l.unwrap())
		.next()
		.unwrap();
    println!("{}", solution(line.trim()));
	
}