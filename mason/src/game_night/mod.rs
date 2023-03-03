
pub fn solution(input: Vec<char>) -> u32 {
    println!("{input:?}");
    let team_counts = count_team_memebers(&input);
    let mut answers = possible_answers(team_counts);
    let (a, b) = ( biggest_diff(&input, &answers.0), biggest_diff(&input, &answers.1));
    println!("Either: {:?}", answers.0);
    println!("Or {:?}", answers.1);
    let best_ans = if a.1 < b.1 {
        answers.0.rotate_right(a.0);
        answers.0
    } else {
        answers.1.rotate_right(b.0);
        answers.1
    };
    println!("{best_ans:?}");
    
    if a.1 < b.1 {
        a.1
    } else {
        b.1
    }
}
type Offset = usize;
type NumberMutations = u32;
fn biggest_diff(input: &Vec<char>, possible_ans: &Vec<char>) -> (Offset, NumberMutations) {
    let mut pos_ans = possible_ans.clone();
    let mut best_offset = 0;
    let mut best_mut: u32 = u32::MAX;

    for i in 0..pos_ans.len() {
        let mut num_mut = 0;
        
        for i in 0..pos_ans.len() {
            if pos_ans[i] != input[i] {
                num_mut += 1;
            }
        }
        if best_mut > num_mut {
            best_offset = i;
            best_mut = num_mut;
        }
        pos_ans.rotate_right(1);
    }
    (best_offset, best_mut)
}

fn possible_answers(team_counts: (u32,u32,u32)) -> (Vec<char>, Vec<char>) {
    let mut ans1 = Vec::new();
    let mut ans2 = Vec::new();
    for _ in 0..team_counts.0 {
        ans1.push('A');
        ans2.push('A');
    }
    for _ in 0..team_counts.1 {
        ans1.push('B');
        ans2.push('C');
    }
    for _ in 0..team_counts.2 {
        ans1.push('C');
        ans2.push('B');
    }
    (ans1, ans2)
}

fn count_team_memebers(input: &Vec<char>) -> (u32, u32, u32) {
    let mut team_counts = (0,0,0);
    for team in input {
        match team {
            'A' => team_counts.0 += 1,
            'B' => team_counts.1 += 1,
            'C' => team_counts.2 += 1,
            _ => unreachable!("Wrong input")
        }
    }
    team_counts
}

fn str_to_char<S: AsRef<str>>(string: S) -> Vec<char> {
    string.as_ref().chars().collect::<Vec<char>>()
}

#[cfg(test)]
mod tests {
    use super::{str_to_char, solution};
    #[test]
    fn example1() {
        let input = str_to_char("ABABC");
        let ans = solution(input);
        assert_eq!(ans, 2);
    }
    #[test]
    fn example2() {
        let input = str_to_char("ABABC");
        let ans = solution(input);
        assert_eq!(ans, 6);
    }
    #[test]
    fn example3() {
        let input = str_to_char("ABCABCABCABC");
        let ans = solution(input);
        assert_eq!(ans, 0);
    }
    #[test]
    fn example4() {
        let input = str_to_char("ACBA");
        let ans = solution(input);
        assert_eq!(ans, 2);
    }
    #[test]
    fn example5() {
        let input = str_to_char("BABABA");
        let ans = solution(input);
        assert_eq!(ans, 3);
    }
}