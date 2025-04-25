// final class can't be extended, also final methods.
public final class ImmutableClass {

    private int value;

    // not definingn constructor gives a default one. So define and make it private.
    private ImmutableClass() {}

    public static ImmutableClass build(int value) {
        ImmutableClass obj = new ImmutableClass();
        obj.value = value;
        return obj;
    }

    public int getValue() {
        return value;
    }

    // Immutable class with no constructor
    public static void main(String[] args) {

        //start program
        ImmutableClass obj = ImmutableClass.build(6);

        ImmutableClass obj2 = new ImmutableClass();//.build(6);
        System.out.println(obj.getValue());
            System.out.println(obj2.getValue());

        }
}