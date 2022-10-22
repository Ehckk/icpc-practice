pub fn goof(sequence: &[char]) -> usize {
    let mut folded = sequence;
    // println!("Original fold: {folded:?}");
    loop {
        if let Some(_folded) = _fold(folded) {
            folded = _folded;
            println!("Pointer to folded: {:#X}", std::ptr::addr_of!(folded) as usize);
        }
        else {
            return folded.len();
        }
    }
}


/// If sequence can be folded, return Some containing the slice as folded
/// If sequence cannot be folded, return None
fn _fold(seq: &[char]) -> Option<&[char]> {
    let len = seq.len();
    if len < 2 {
        return None;
    }
    let mut left_pal: Option<usize> = None;
    let mut right_pal: Option<usize> = None;

    let mut left_letter_idx = 0;
    while left_letter_idx < len / 2 {
        // Find the furthest set of double letters that make a palindrome as long as it starts from the left
        if seq[left_letter_idx] == seq[left_letter_idx + 1] { // letters match
            // If palindrome, save idx of next right letter
            if is_palindrome(&seq[..=(left_letter_idx*2+1)]) {
                left_pal = Some(left_letter_idx+1);
            }
            // If we've found a palindrome and these double letters we're in one, we've already found
            // The longest from the left
            else if left_pal.is_some() {
                break;
            }
        }
        left_letter_idx += 1;
    }
    let mut right_letter_idx = len - 1;
    while right_letter_idx > len / 2 {
        // Find the furthest set of double letters that make a palindrome as long as it starts from the right
        if seq[right_letter_idx] == seq[right_letter_idx - 1] { // letters match
            // If palindrome, save idx of next right letter
            if is_palindrome(&seq[(right_letter_idx*2 - len)..]) {
                right_pal = Some(right_letter_idx-1);
            }
            // If we've found a palindrome and these double letters we're in one, we've already found
            // The longest from the left
            else if left_pal.is_some() {
                break;
            }
        }
        if right_letter_idx == 0 {
            break;
        }
        right_letter_idx -= 1;
    }
    // println!("{seq:?}");
    // println!("Left pal len: {:?}, Right pal len: {:?}", left_pal_len, right_pal_len);
    match (left_pal, right_pal) {
        // Left and right side have palindromes
        (Some(l), Some(r)) => {
            if l >= (len - r - 1) {
                Some(&seq[l..])
            }
            else {
                Some(&seq[..=r])
            }
        },
        (Some(l),None) => {
            Some(&seq[l..])
        }
        (None, Some(r)) => {
            Some(&seq[..=r])
        }
        (None, None) => {
            None
        }
    }
}

/// returns true if the entire sequence is a palindrome
fn is_palindrome(seq: &[char]) -> bool {
    // println!("Is {seq:?} a pal?");
    let len = seq.len();
    let mut left = 0; 
    let mut right = len-1;
    // check each 
    while left <= right {
        if seq[left] != seq[right] {
            return false;
        }
        left += 1;
        right -= 1;
    }
    true
}


pub fn recursive_goof(seq: &[char]) -> usize {
    let len = seq.len();
    if len < 2 {
        return len;
    }
    let mut left_pal: Option<usize> = None;
    let mut right_pal: Option<usize> = None;

    let mut left_letter_idx = 0;
    while left_letter_idx < len / 2 {
        // Find the furthest set of double letters that make a palindrome as long as it starts from the left
        if seq[left_letter_idx] == seq[left_letter_idx + 1] { // letters match
            // If palindrome, save idx of next right letter
            if is_palindrome(&seq[..=(left_letter_idx*2+1)]) {
                left_pal = Some(left_letter_idx+1);
            }
            // If we've found a palindrome and these double letters we're in one, we've already found
            // The longest from the left
            else if left_pal.is_some() {
                break;
            }
        }
        left_letter_idx += 1;
    }
    let mut right_letter_idx = len - 1;
    while right_letter_idx > len / 2 {
        // Find the furthest set of double letters that make a palindrome as long as it starts from the right
        if seq[right_letter_idx] == seq[right_letter_idx - 1] { // letters match
            // If palindrome, save idx of next right letter
            if is_palindrome(&seq[(right_letter_idx*2 - len)..]) {
                right_pal = Some(right_letter_idx-1);
            }
            // If we've found a palindrome and these double letters we're in one, we've already found
            // The longest from the left
            else if right_pal.is_some() {
                break;
            }
        }
        if right_letter_idx == 0 {
            break;
        }
        right_letter_idx -= 1;
    }
    // println!("{seq:?}");
    // println!("Left pal len: {:?}, Right pal len: {:?}", left_pal_len, right_pal_len);
    match (left_pal, right_pal) {
        // Left and right side have palindromes
        (Some(l), Some(r)) => {
            if l >= (len - r - 1) {
                recursive_goof(&seq[l..])
            }
            else {
                recursive_goof(&seq[..=r])
            }
        },
        (Some(l),None) => {
            recursive_goof(&seq[l..])
        }
        (None, Some(r)) => {
            recursive_goof(&seq[..=r])
        }
        (None, None) => {
            len
        }
    }
}


#[cfg(test)]
mod tests {
    use crate::goof::{recursive_goof, goof};

    use super::is_palindrome;

    fn test_palindrome_helper<S: Into<String>>(s: S) -> bool {
        let chars: Vec<char> = s.into().chars().collect();
        if chars.len() % 2 != 0 {
            return false;
        }
        is_palindrome(&chars)
    }

    #[test]
    fn test_palindromes() {
        // Regular palindrome
        assert!(test_palindrome_helper("ATTA"));
        // Extra letter on ends
        assert!(!test_palindrome_helper("ATTAA"));
        assert!(!test_palindrome_helper("AATTA"));
        // Repeating
        assert!(!test_palindrome_helper("CGCG"));
        // Actual palindrome
        assert!(test_palindrome_helper("CGGC"));
    }

    #[test]
    fn test_recurse_fold() {
        let chars: Vec<char> = "ATTACC".chars().collect();
        assert_eq!(recursive_goof(&chars), 3);

        let chars: Vec<char> = "AAAAGAATTAA".chars().collect();
        assert_eq!(recursive_goof(&chars), 5);
    }

    #[test]
    fn test_nonrecurse_fold() {
        let chars: Vec<char> = "ATTACC".chars().collect();
        assert_eq!(goof(&chars), 3);

        let chars: Vec<char> = "AAAAGAATTAA".chars().collect();
        assert_eq!(goof(&chars), 5);
    }
}