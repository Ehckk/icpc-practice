

pub fn solution(input: String) -> String {
    
    let numbers = input.lines().flat_map(|l| l.trim().parse()).collect::<Vec<i32>>();
    let last_num = numbers.last().unwrap();
    let rest = &numbers[1..];
    let mut missing_nums = Vec::new();
    for i in 1..=*last_num {
            if !rest.contains(&i) {
                    missing_nums.push(i);
                }
        }


    if missing_nums.is_empty() {
            String::from("good job")
        }
    else {
            missing_nums.iter().map(|n| n.to_string()).collect::<Vec<String>>().join("\n")
        }
    
}


#[cfg(test)]
mod test {
    use super::solution;

    #[test]
    fn input1() {
        let input = r#"9
2
4
5
7
8
9
10
11
13
"#;
        println!("{input}");
        let output = r#"1
3
6
12"#;
        assert_eq!(solution(
			input.into()
		), 
			output);
    }
    #[test]
    fn input2() {
        let input = r#"5
1
2
3
4
5
"#;
        println!("{input}");
        let output = r#"good job"#;
        assert_eq!(solution(
			input.into()
		), 
			output);
    }


}