

pub fn solution<S: AsRef<str>>(input: S) -> String {
	let input = Input::from_str(input);
	let first_indices = get_first_tower_indices(&input);
	let second_indices = get_second_indices(first_indices);
	let mut first_tower = input.get_sorted_tower(first_indices);
	let mut second_tower = input.get_sorted_tower(second_indices);
	first_tower.append(&mut second_tower);
	first_tower
		.iter()
		.map(|num| num.to_string())
		.collect::<Vec<_>>()
		.join(" ")
}

fn get_first_tower_indices(input: &Input) -> (usize,usize, usize) {
	let len = input.boxes.len();
	for i in 0..len {
		for j in 1..len {
			for k in 2..len {
				let box1 = input.boxes[i];
				let box2 = input.boxes[j];
				let box3 = input.boxes[k];
				if box1 + box2 + box3 == input.towers.0 {
					return (i, j, k)
				}
			}
		}
	}
	unreachable!("Bad input")
}

fn get_second_indices(first_indices: (usize, usize, usize)) -> (usize, usize, usize) {
	let mut indices = vec![];
	for i in 0..8 {
		if i == first_indices.0 || i == first_indices.1 || i == first_indices.2 {
			continue;
		}
		indices.push(i);
	}
	(indices[0], indices[1], indices[2])
}

#[derive(Debug)]
struct Input {
	boxes: Vec<i32>,
	towers: (i32, i32),
}

impl Input {
	fn from_str<S: AsRef<str>>(input: S) -> Self {
		let nums = input.as_ref()
			.split(" ")
			.map(|num| num.parse::<i32>().unwrap())
			.collect::<Vec<i32>>();
		Self {
			boxes: nums[..6].into(),
			towers: (nums[6], nums[7]),
		}
	}

	fn get_sorted_tower(&self, indices: (usize, usize, usize)) -> Vec<i32> {
		let mut final_boxes = Vec::new();
		for (i, boxx) in self.boxes.iter().enumerate() {
			if i == indices.0 || i == indices.1 || i == indices.2 {
				final_boxes.push(*boxx);
			}
		}
		final_boxes.sort_by(|a, b| b.cmp(a));
		final_boxes
	}
}



#[cfg(test)]
mod tests {
    use super::solution;

	#[test]
	fn example1() {
		let input = "12 8 2 4 10 3 25 14";
		let output = solution(input);
		assert_eq!(output, "12 10 3 8 4 2")
	}

	
	#[test]
	fn example2() {
		let input = "12 17 36 37 51 63 92 124";
		let output = solution(input);
		assert_eq!(output, "63 17 12 51 37 36")
	}
}