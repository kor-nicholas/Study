package quorters;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

// SOURCE - annotation work only in source, in bytecode it isn't (@Override)
// CLASS - annotation is in bytecode, but you can't use it in runtime with help reflection (default)
// RUNTIME - annotation is in bytecode, you can use it in runtime with reflection
@Retention(RetentionPolicy.RUNTIME)
public @interface InjectRandomInt {
    int min();

    int max();
}