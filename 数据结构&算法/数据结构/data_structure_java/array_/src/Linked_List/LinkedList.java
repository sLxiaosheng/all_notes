package Linked_List;

import java.util.IllformedLocaleException;

public class LinkedList<E> {


    //内部类
    //将节点设置为私有
    private class Node{
        //设置为公开
        //存放数据
        public E e;
        public Node next;

        public Node(E e, Node next){
            //将用户传来的数据转为节点，链接
            this.e = e;
            this.next = next;
        }

        public Node(E e){
            this(e, null);
        }

        public Node(){
            this(null, null);
        }

        @Override
        public String toString(){
            return e.toString();
        }
    }

    //设置虚拟节点
    private Node dummyHead;
    int size;

    public LinkedList(){

        //虚拟节点，属性都为空
        dummyHead = new Node(null, null);
        size = 0;
    }

    //获取元素个数
    public int getSize(){
        return size;
    }

    //检查是否为空
    public boolean isEmpty(){

        return size == 0;
    }

    //插入元素
    public void addElement(int index, E e){

        if(index < 0 || index > size)
            throw new IllformedLocaleException("Add failed. Illegal index.");


        Node prev = dummyHead;
        for(int i = 0;i < index ; i ++){
            prev = prev.next;
        }
        Node node = new Node(e);
        node.next = prev.next;
        prev.next = node;

        size ++;
    }

    //在链表添加新元素
    public void addFirst(E e){

        addElement(0, e);
    }

    //在链表尾部添加新元素
    public void addLast(E e){
        addElement(size, e);
    }

    //获取链表第index个元素
    public E get(int index){

        if (index < 0 || index >= size)
            throw new IllegalArgumentException("Get failed. Illegal index.");

        Node cur = dummyHead.next;
        for (int i = 0; i < index; i ++)
            cur = cur.next;

        return cur.e;
    }

    //获取链表的第一个元素
    public E getFirst(){
        return get(0);
    }

    //获得链表的最后一个元素
    public E getLast(){
        return get(size - 1);
    }

    //修改链表的第index元素，改为e
    public void update(int index, E e){

        if (index < 0 || index >= size)
            throw new IllegalArgumentException("update failed. Illegal index.");

        Node cur = dummyHead.next;
        for (int i = 0; i < index; i ++)
            cur = cur.next;

        cur.e = e;
    }

    //查找链表中是否有元素e
    public boolean contains(E e){

        Node cur = dummyHead.next;
        while(cur != null){
            if(cur.e.equals(e))
                return true;
            cur = cur.next;
        }
        return false;
    }

    //在链表中删除index位置的元素，返回删除的元素
    public E deleteElement(int index){

        if (index < 0 || index >= size)
            throw new IllegalArgumentException("Get failed. Illegal index.");

        Node prev = dummyHead;
        for(int i = 0; i < index; i ++)
            prev = prev.next;

        Node retNode = prev.next;
        prev.next = retNode.next;
        retNode.next = null;
        size --;

        return retNode.e;
    }

    //删除第一个元素
    public void deleteFirst(){
        deleteElement(0);
    }
    //删除最后一个元素
    public void deleteLast(){
        deleteElement(size - 1);
    }

    //将链表转换为字符串
    @Override
    public String toString(){

        StringBuilder res = new StringBuilder();

        Node cur = dummyHead.next;
        while(cur != null){
            res.append(cur + "->");
            cur = cur.next;
        }
        //与上面等价
//        for(Node cur = dummyHead.next; cur != null; cur = cur.next)
//            res.append(cur + "->");
//        res.append("NULL");

        res.append("NULL");

        return res.toString();
    }
}
