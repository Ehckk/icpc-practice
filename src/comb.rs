
#[derive(Debug)]
pub struct Combinations<T: Clone> {
    choices: Vec<T>,
    buffer: Vec<T>,
    pub num_combs: usize,
    i: usize,
}


impl<T> Combinations<T> where T: Clone {
    pub fn from_choices(choices: Vec<T>, size: usize) -> Self {
        let clo = choices.clone();
        let t = clo[0].clone();
        Self {
            choices,
            buffer: vec![t.clone(); size],
            num_combs: clo.len().pow(size as u32),
            i: 0,
        }
    }
}

impl<T> Iterator for Combinations<T> where T: Clone {
    type Item = Vec<T>;

    fn next(&mut self) -> Option<Self::Item> {
        let len = self.buffer.len();
        if self.i >= self.num_combs {
            return None;
        }
        let base = self.choices.len();
        
        for i in 0..(self.buffer.len()) {
            let choice = self.i/base.pow(i as u32) % base;
            self.buffer[len - i - 1] = self.choices[choice].clone();
        }
        self.i += 1;
        Some(self.buffer.clone())
    }
}

#[cfg(test)]
mod tests {
    use super::Combinations;

    #[test]
    fn test_single_len_comb_iterator() {
        let actual = [
            ['A'], 
            ['B'], 
            ['C'],
        ];
        let combs = Combinations::from_choices(vec!['A', 'B', 'C'], 1);
        println!("{combs:?}");
        for (i, comb) in combs.enumerate() {
            println!("{comb:?}");
            assert_eq!(actual[i].to_vec(), comb);
        }
    }

    #[test]
    fn test_two_len_comb_iterator() {
        let actual = [
            ['A', 'A'],
            ['A', 'B'],
            ['A', 'C'],
            ['B', 'A'],
            ['B', 'B'],
            ['B', 'C'],
            ['C', 'A'],
            ['C', 'B'],
            ['C', 'C'],
        ];
        let combs = Combinations::from_choices(vec!['A', 'B', 'C'], 2);
        println!("{combs:?}");
        for (i, comb) in combs.enumerate() {
            println!("{comb:?}");
            assert_eq!(actual[i].to_vec(), comb);
        }
    }
}