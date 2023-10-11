package quorters;

import org.springframework.context.support.ClassPathXmlApplicationContext;

//@SpringBootApplication
public class Main {
    // XmlBeanDefinitionReader (read from context.xml) -> BeanDefinitions (Map<BeanId, Declaration>)
    // BeanFactory (create classes, save beans in IoC container)
    public static void main(String[] args) throws InterruptedException {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("context.xml");
//        SpringApplication.run(Main.class);
//        while (true) {
//            Thread.sleep(100);
////            context.getBean(TerminatorQuoter.class).sayQuote(); // use class is not wright
//            context.getBean(Quoter.class).sayQuote(); // because we can get proxy-class
//        }
    }

    // BeanFactory gives object to BeanPostProcessor

    // BeanPostProcessor (set beans before they are in IoC container)
    // 1. BeanPostProcessors set our beans
    // 2. work init-method
    // 3. BeansPostProcessors set beans again

    // @Profiling (we need to change object in runtime)
    // or sglib - extends real class
    // or dynamic proxy - implement interfaces like real class (better, because class can have final)
    // AOP -> if class has interfaces - dynamic proxy; else - sglib

    // ApplicationListener (use to set something after constructor and PostConstruct):
    // 1. ContextStartedEvent (start set context)
    // 2. ContextStoppedEvent (stop set context)
    // 3. ContextRefreshEvent (after stop - context refresh)
    // 4. ContextClosedEvent
}
