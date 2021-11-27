package sample;

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        // user input
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String fileName = "demo.txt";

        // file input
        BufferedReader fileInput = new BufferedReader(new FileReader("src/resources/" + fileName));

        String line;

        while((line = fileInput.readLine())!= null){

            String[] words = line.split(" ");
            char[] charArr = line.toCharArray();
            StringJoiner joiner = new StringJoiner(" ");
            int pnc = 0;
            int vowel = 0;


            for(char c: charArr) {
                if (c == ',' || c == '!' || c == ':' || c == '.' || c == '?' || c == '-') pnc++;

                String cc = String.valueOf(c);
                cc = cc.toLowerCase();

                if (cc.equals("a") || cc.equals("e") || cc.equals("i") || cc.equals("o") || cc.equals("u")){
                    vowel++;
                }
            }


            for (String word: words){

                char[] charWord = word.toCharArray();

                for(char c: charWord){
                    String cc = String.valueOf(c);
                    cc = cc.toLowerCase();

                    if (cc.equals("a") || cc.equals("e") || cc.equals("i") || cc.equals("o") || cc.equals("u")){
                        word = word.replace(cc, "#");
                    }
                }

                System.out.println("After: " + word);
                joiner.add(word);
            }

            System.out.println("\nLine:- " + line );
            System.out.println("Words:- " + words.length);
            System.out.println("Total Punctuation:- " + pnc);
            System.out.println("Total Vowel:- " + vowel);

            String sbb = joiner.toString();
            System.out.println("New String: " + sbb + " --Type: " + sbb.getClass().getName());
        }
    }
}
