package quorters;

import jakarta.annotation.PostConstruct;

// our annotation to profile (execute code) for all methods
// sout time before and after execute every method
@Profiling
public class TerminatorQuoter implements Quoter {
    @InjectRandomInt(min = 1, max = 10)
    private int repeat;
    private String message;

    // PostConstruct - annotation to initialize init-method for Spring (but need to write annotation in context.xml)
    // (or use namespace to annotation work)
    @PostConstruct
    public void init(){
        System.out.println("Phase 2");
        System.out.println("repeat = " + repeat);
    }

    public TerminatorQuoter() {
        System.out.println("Phase 1");
//        System.out.println(repeat); // 0, because Spring don't set value
    }

    public void setMessage(String message) {
        this.message = message;
    }

    // PostProxy - when all set and proxy works
    @Override
    @PostProxy
    public void sayQuote() {
        System.out.println("Phase 3");
        for (int i = 0; i < repeat; i++) {
            System.out.println("message = " + message);
        }
    }
}
