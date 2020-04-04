package Binary_Search_tree;

import Set.FileOperation;

import java.util.ArrayList;
import java.util.Random;

public class Main {

    public static void main(String[] args){

        System.out.println("Pride and Prejudice");

        ArrayList<String> words1 = new ArrayList<>();
        FileOperation.readFile("pride-and-prejudice.txt", words1);
        System.out.println("Total words: " + words1.size());

        

    }
}
