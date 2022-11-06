const manachers = (s: string) => {
	const chars: string[] = [] // Used to store string with "#" characters (dummy string)
	chars.push("#") // Start by inserting dummy char
	for (const c of s) { 
		chars.push(c) // Insert string char
		chars.push("#") // Inserting dummy char afterwards
		// Ex: 
		//	Input: "ababa"
		//	Output: "#a#b#a#b#a#"
	}
	let start = 0; // Stores start of longest found palindrome 
	let max = 0; // Stores length of longest found palindrome
	let center = 0; // Center character palindrome center
	let right = 0; // Rightmost character of current palindrome
	// The rightmost char and center char pointers are used ONLY for checking for the palindromes
	// The start and max values are used to determine the palindrome

	const lps: number[] = Array(chars.length).fill(0) // Stores longest palindrome length at each character
	// So if lps[4] = 5, then the longest palindromic substring with center point at i = 4 is 5

	for (let i = 0; i < chars.length; i++) { // 2 * s.length + 1 is the length of the dummy string

		// You need to have found at least 1 palindrome greater than size 1 for this part to do anything 
		// You need to have found a nested palindrome within that palindrome for this to do anything meaningful	
		if (i < right) { // This is used to initialize the LPS value for the iteration, if i exceeds the rightmost pointer
			// Given the properties of a palindrome, characters after the center point of a palindrome will match those before it
			// So if we found a nested palindrome prior to the center, we know the smaller palindrome exists on the other side of the center
			// Ex: 
			//	Palindrome "bcacbdbcacb" contains subpalindrome "cac" to the left and right of the center ("d")
			//  Both occurences of the subpalindrome have a center 3 characters to the left/right of "d"
			// Since we have the lengths of subpalindromes before the center stored, we can account for subsequent subpalindromes we previously found

			lps[i] = Math.min(right - i, lps[2 * center - i]) 
			// right - i => maximum possible size of a nested palindrome at i that doesn't go past the right side pointer
			// lps[2 * center - i => the mirror index of the palindrome 
			// Ex: 
			// 	"cdadcdadb" => "#c#d#a#d#c#d#a#d#b#"
			// 	As of i = 10, lps = [0,1,0,1,0,5,0,1,0,7,0,0,0,0,0,0,0,0,0], max = 7, start = 2, center = 9 right = 16
			// 	i = 11, 11 < 16
			//	right - i = 5
			// 	lps[(2 * 9) - 11] = lps[7] = 1 ("d")
			//	1 is smaller, so lps[11]  = 1
			// 	Nothing else interesting happens
			// 	i = 12, 12 < 16
			//	right - i = 4
			// 	lps[(2 * 9) - 12] = lps[6] = 0 ("#")
			//	0 is smaller, so lps[12]  = 0
			// 	Nothing else interesting happens
			//  i = 13, 13 < 16
			//	right - i = 3
			//	lps[(2 * 9) - 13] = lps[5] = 5 ("cdadc" around first "a")
			// 	The palindrome around i = 5 contains characters from outside the larger palindrome around i = 9
			//	However, we can't fit a nested palindrome of size 5 about i = 13, within the right pointer bound of 16, so we set lps[13] to 3
			//	Our palindrome checking loop doesn't run, since it immediately checks lps[9] ("c") and lps[17] ("b"), which do not match
			// This is the algorithm's magic at work 
		} 
		// Otherwise, lps[i] starts at 0
		// Which is weird because most of the times i < right, lps[i] will be set to zero or 1 anyways, unless it is the center of a nested palidnrome

		while (chars[i - lps[i] - 1] === chars[i + lps[i] + 1]) { // In short, this is the palindrome check
			lps[i] += 1; // Increments LPS value to index characters from itself as the center point 
			// Compares left-hand and right-hand characters based on the current LPS value for center point i
			// 	So if our center is at i = 2, the first iteration compares chars[1] and chars[3] since lps[i] starts at 0
			// 	If they match, lps[i] is incremented and the loop continues
			// 	Next loop compares chars[0] and chars[4]
			
			// LPS will always start at 0 for "#", and 1 for characters present in the original string
			// Ex 1:
			//	Say our string is "duck"
			//	Our dummy string will then be "#d#u#c#k#"
			// 	When we compare on any string character as the center, we compare between two hashes, incrementing LPS at least once
			// 	When we compare on any dummy character as the center, we compare between two string characters, which may or may not increment LPS

			// Ex 2:
			//	Say our string is "ababba"
			//	Our dummy string will then be "#a#b#a#b#b#a#"
			//	i = 0 is the start of the string, nothing interesting happens there, and lps[0] = 0 
			// 	At i = 1, we compare two "#" chars at positions 0 and 2, so lps[1] is incremented
			//	Next iteration, we compare positions -1 and 3
			// 	In JS/TS, negative indicies return undefined, breaking the loop
			//	But normally this would compare "#" (last character) and "b", so the loop breaks anyways

			// Ex 3:
			//	Say our string is "attacc"
			// 	Our dummy string will then be "#a#t#t#a#c#c#"
			// 	From i = 0 to i = 3 we don't have anything special
			//	So far: lps = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
			//	At i = 4, we get "#a#t#t#a#"
			//	Loop breaks when lps[4] = 4, when we compare pos -1 ("#") and pos 9 ("c") 
			// Notice how the loop properly executes regardless of whether the center is a string character or dummy character

			// One cool thing about this palindrome check is that it is done completely independent of stored start/max and center/right pointers
			// It only uses the i and lps array 
		}

		if (i + lps[i] > right) { // If we checked characters past the value of the right hand pointer, we need to update our pointers
			center = i // Update center pointer to i, the most recently checked center point
			right = i + lps[i] // Update right pointer to rightmost checked index 
		}

		if (lps[i] > max) { // If we found a palindrome with length greater than the max, we update our values
			start = Math.abs(Math.ceil((i - lps[i] - 1) / 2)) // This line of code calculates the start index (thanks JS numbers)
			max = lps[i] // Updating the max length using the stored lps value for center point i
			
		}
	}
	console.log(s);
	console.log(lps);
	return s.slice(start, start + max)	
	// Recap
	//	1. Insert dummy characters into a dummy string, such that a string of length n becomes a dummy string of length 2n + 1
	// 	2. Initialize values for start and length of biggest palindrome and pointers for center and right bound of current palindrome
	// 	3. Initialize LPS integer array of length 2n + 1
	// 	4. Loop over each character at each position in the dummy string, i
	//	5. Compare the characters i - lps[i] - 1 (left) and i + lps[i] + 1 (right)
	// 	6. Increment lps[i] if they match, repeat until they do not match
	// 	7. If i + lps[i] > right bound, update the center pointer to i and right bound to i + lps[i]
	//	8. If lps[i] > length, set next max length value to lps[i], and start value to (i - lps[i] / 2)
	// 	10. On subsequent loops, if i < right bound, set lps[i] to the mmin value between right bound - i and lps[(2 * center) - i]
	// 	11. After iterating over the string, your longest substring can be found using the start and max length values	
}
console.log(manachers("abababbc"))
console.log(manachers("attacc"))
console.log(manachers("cdadcdadb"))