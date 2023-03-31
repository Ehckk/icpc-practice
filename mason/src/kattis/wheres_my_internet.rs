use std::collections::{HashMap, HashSet};


pub fn solution(input: String) -> String {
    let nums: Vec<(usize, usize)> = input
        .lines()
        .map(|l| {
            let mut split = l.trim().split(" ");
            (split.next().unwrap().parse::<usize>().unwrap(), 
                split.next().unwrap().parse::<usize>().unwrap())
        }).collect();
    let (num_houses, num_cables) = nums.first().unwrap();
    let pairs = &nums[1..];
    let tree = Tree::build_tree(*num_houses, *num_cables, pairs);
    let connected = tree.find_connected();
    println!("{connected:?}");
    let mut unconnected = Vec::with_capacity(*num_houses);
    for i in 1..=*num_houses {
        if !connected.contains(&i) {
            unconnected.push(i);
        }
    }

    if unconnected.is_empty() {
        String::from("Connected")
    }
    else {
        unconnected
            .into_iter()
            .map(|house| {
                format!("{}", house)
            })
            .collect::<Vec<String>>()
            .join("\n")
    }
}

struct Tree {
    branches: Vec<Vec<usize>>,
}

impl Tree {
    fn build_tree(num_houses: usize, num_cables: usize, pairs: &[(usize, usize)]) -> Self {
        let mut tree = Self {
            branches: vec![vec![]; num_houses],
        };
        for (from, to) in pairs {
            tree.branches[from-1].push(*to);
            tree.branches[to-1].push(*from);
        }
        println!("{:?}", tree.branches);
        tree
    }

    fn find_connected(&self) -> HashSet<usize> {
        let mut visited: HashSet<usize> = HashSet::with_capacity(self.branches.len()+1);
        visited.insert(1);

        let mut queue = Vec::new();
        queue.push(1usize);
        while !queue.is_empty() {
            let next = queue.pop().unwrap();
            // if already visited, continue;
            visited.insert(next);
            for connected in &self.branches[next-1] {
                if visited.contains(&connected) {
                    continue;
                }
                queue.push(*connected);
            }
        }
        visited
    }
}


#[cfg(test)]
mod test {
    use super::solution;

    #[test]
    fn input1() {
        let input = r#"6 4
1 2
2 3
3 4
5 6
"#;
        println!("{input}");
        let output = r#"5
6"#;
        assert_eq!(solution(
			input.into()
		), 
			output);
    }
    #[test]
    fn input2() {
        let input = r#"2 1
2 1
"#;
        println!("{input}");
        let output = r#"Connected"#;
        assert_eq!(solution(
			input.into()
		), 
			output);
    }

    #[test]
    fn input3() {
        let input = r#"4 3
2 3
4 2
3 4
"#;
        println!("{input}");
        let output = r#"2
3
4"#;
        assert_eq!(solution(
			input.into()
		), 
			output);
    }

}