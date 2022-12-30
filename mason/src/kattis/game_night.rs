
pub fn solution(input: String) -> u32 {
    let data = ProblemData::from_input(input);
    let counts = data.team_counts();

    let mut best_variation1 = Vec::new();
    let mut best_variation2 = Vec::new();
    for _ in 0..counts.0 {
        best_variation1.push(Team::A);
        best_variation2.push(Team::A);
    }
    for _ in 0..counts.1 {
        best_variation1.push(Team::B);
        best_variation2.push(Team::C);
    }
    for _ in 0..counts.2 {
        best_variation1.push(Team::C);
        best_variation2.push(Team::B);
    }
    let mut best = u32::MAX;
    for i in 0..=data.count {
        let diff = data.determine_disimilarity(&best_variation1);
        if diff < best {
            best = diff
        }
        let diff = data.determine_disimilarity(&best_variation2);
        if diff < best {
            best = diff
        }
        best_variation1.rotate_right(1);
        best_variation2.rotate_right(1);
    }
    best
}

struct ProblemData {
    pub count: u32,
    pub arangement: Vec<Team>,
}

impl ProblemData {
    fn from_input<S: AsRef<str>>(input: S) -> Self {
        let mut parts = input.as_ref().lines();
        // Read count
        let count: u32 = parts.next().unwrap().parse().unwrap();
        // Read team member arangement
        let mut arangement = Vec::new();
        for ch in parts.next().unwrap().trim().chars() {
            let team = match ch {
                'A' => Team::A,
                'B' => Team::B,
                'C' => Team::C,
                _ => panic!("Invalid team: {ch}"),
            };
            arangement.push(team);
        }
        Self {
            count,
            arangement,
        }
    }

    fn team_counts(&self) -> (u32, u32, u32) {
        let mut counts = (0,0,0);
        for team in &self.arangement {
            match team {
                Team::A => counts.0 += 1,
                Team::B => counts.1 += 1,
                Team::C => counts.2 += 1,
            }
        }
        counts
    }

    fn determine_disimilarity(&self, arrangement: &Vec<Team>) -> u32 {
        let mut diff_count = 0;
        for (team1, team2) in self.arangement.iter().zip(arrangement) {
            if team1 != team2 {
                diff_count += 1;
            }
        }
        diff_count
    }
}

#[derive(PartialEq)]
enum Team {
    A,
    B,
    C,
}


#[cfg(test)]
mod test {
    use crate::kattis::game_night::solution;

    #[test]
    fn input1() {
        let input = r#"5
        ABABC"#;
        println!("{input}");
        let output = 2;
        assert_eq!(solution(input.into()), output);
    }

    #[test]
    fn input2() {
        let input = r#"12
        ABCABCABCABC"#;
        println!("{input}");
        let output = 6;
        assert_eq!(solution(input.into()), output);
    }

    #[test]
    fn input3() {
        let input = r#"4
        ACBA"#;
        println!("{input}");
        let output = 0;
        assert_eq!(solution(input.into()), output);
    }

    #[test]
    fn input4() {
        let input = r#"6
        BABABA"#;
        println!("{input}");
        let output = 2;
        assert_eq!(solution(input.into()), output);
    }

    #[test]
    fn input5() {
        let input = r#"9
        ABABCBCAC"#;
        println!("{input}");
        let output = 3;
        assert_eq!(solution(input.into()), output);
    }
}