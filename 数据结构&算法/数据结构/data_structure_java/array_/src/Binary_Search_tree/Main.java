package Binary_Search_tree;

import java.util.ArrayList;
import java.util.Random;

public class Main {

    public static void main(String[] args){

        BST<Integer> bst = new BST<>();
        int[] nums = {5, 3, 6, 8, 4, 2};
        //创造树
        for(int num: nums)
            bst.add(num);

        //遍历树
        bst.preOrder();
        System.out.println();
        System.out.println(bst);

        //遍历树
        bst.inOrder();
        System.out.println();
        System.out.println(bst);

        //遍历树
        bst.postOrder();
        System.out.println();
        System.out.println(bst);

        //非递归
        bst.preOrderNR();
        System.out.println();

        bst.leveOrder();
        System.out.println();



        //找到最值
        System.out.println(bst.minimum());
        System.out.println(bst.maximum());

        //自己写的
        bst.deleteMax();
        System.out.println(bst);

        bst.deleteMin();
        System.out.println(bst);


        BST<Integer> bst1 = new BST<>();
        Random random = new Random();

        int n = 1000;

        for(int i = 0; i < n; i ++)
            bst1.add(random.nextInt(10000));

        ArrayList<Integer> nums1 = new ArrayList<>();
        while(!bst.isEmpty())
            nums1.add(bst.removeMin());

        System.out.println(nums1);
        for(int i = 1; i < nums1.size(); i ++)
            
    }
}
