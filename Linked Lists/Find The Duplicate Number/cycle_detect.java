class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> set = new HashSet();
        ListNode root = head;

        while (root != null) {
            if (set.contains(root)) {
                return true;
            }

            set.add(root);
            root = root.next;
        }

        return false;
    }
}
