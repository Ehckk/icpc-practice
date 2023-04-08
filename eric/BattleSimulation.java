import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;

class BattleSimulation {
    private HashMap<Character, Character> counterMap = new HashMap<Character, Character>();
    private HashMap<Character, Integer> comboMap = new HashMap<Character, Integer>();
    private ArrayDeque<Character> window = new ArrayDeque<Character>();
    private ArrayList<Character> counterMoves = new ArrayList<Character>();
    private char[] moves;

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        
        BattleSimulation battleSim = new BattleSimulation();
        battleSim.readInput(scnr);
        scnr.close();

        battleSim.simulateBattle();
    }

    public void readInput(Scanner scnr) {
        moves = scnr.nextLine().trim().toCharArray();
        counterMap.put('R', 'S');
        counterMap.put('B', 'K');
        counterMap.put('L', 'H');
        comboMap.put('R', 0);
        comboMap.put('B', 0);
        comboMap.put('L', 0);
    }

    public void simulateBattle() {
        for (char move : moves) {
            // System.out.println(move);
            // System.out.printf("R: %d\tB: %d\tL: %d %n", comboMap.get('R'), comboMap.get('B'), comboMap.get('L'));
            if (window.size() == 3) {
                if (isCombo()) {
                    while (window.size() > 0) {
                        char removed = window.pop();
                        comboMap.put(removed, comboMap.get(removed) - 1);
                    }
                    counterMoves.add('C');
                } else {
                    char removed = window.pop();
                    comboMap.put(removed, comboMap.get(removed) - 1);
                    counterMoves.add(counterMap.get(removed));
                }
            }
            window.add(move);
            comboMap.put(move, comboMap.get(move) + 1);
        }
        if (isCombo()) {
            counterMoves.add('C');
        } else {
            while (window.size() > 0) {
                Character removed = window.pop();
                counterMoves.add(counterMap.get(removed));
            }
        }
        
        StringBuilder output = new StringBuilder(); 
        for (int i = 0; i < counterMoves.size(); i++) {
            output.append(counterMoves.get(i));
        }
        String outputStr = new String(output);
        System.out.println(outputStr);
    }

    public boolean isCombo() {
        if (comboMap.get('R') != 1) return false;
        if (comboMap.get('B') != 1) return false;
        return comboMap.get('L') == 1; 
    }
}
