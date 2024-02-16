import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class NoDuplicates {
    Set<String> set = new HashSet<String>();

    public static void main(String[] args) {
        NoDuplicates solution = new NoDuplicates();
        System.out.println(solution.solve());
    }

    String solve() {
        Scanner scnr = new Scanner(System.in);
        String[] words = scnr.nextLine().trim().split(" ");
        Collections.addAll(set, words);
        scnr.close();

        if (set.size() == words.length) {
            return "yes";
        }
        return "no";
    }
}