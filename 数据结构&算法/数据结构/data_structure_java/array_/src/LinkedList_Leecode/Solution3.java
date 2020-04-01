package LinkedList_Leecode;

import Linked_List.LinkedList;

public class Solution3 {

    public ListNode removeElements(ListNode head, int val) {


        //最基本的问题
        if(head == null)
            return null;

        ListNode res = removeElements(head.next, val);
        if(head.val == val){
            System.out.println(res);
            return res;
        }
        else{
            head.next = res;
            return head;
        }

    }

    public static void main(String[] args){

        int[] nums = {1, 2, 3, 4, 5, 6};
        ListNode head = new ListNode(nums);
        System.out.println(head);

        ListNode res = (new Solution3()).removeElements(head, 2);
        System.out.println(res);
        System.out.println(res);

    }
}
