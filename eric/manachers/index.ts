const manachers2 = (s: string) => {
	const chars: string[] = []
	chars.push("#")
	for (const c of s) { 
		chars.push(c)
		chars.push("#") 
	}
	let start = 0;
	let max = 0;
	let center = 0;
	let right = 0; 
	const lps: number[] = Array(chars.length).fill(0) 
	for (let i = 0; i < chars.length; i++) { 
		if (i < right) { 
			lps[i] = Math.min(right - i, lps[2 * center - i]) 
		}
		while (chars[i - lps[i] - 1] === chars[i + lps[i] + 1]) { 
			lps[i] += 1; 
		}
		if (i + lps[i] > right) { 
			center = i 
			right = i + lps[i] 
		}
		if (lps[i] > max) { 
			start = Math.abs(Math.ceil((i - lps[i] - 1) / 2)) 
			max = lps[i] 	
		}
	}
	console.log(s);
	console.log(lps);
	return s.slice(start, start + max)	
}
console.log(manachers2("abababbc"))
console.log(manachers2("attacc"))
console.log(manachers2("cdadcdadb"))