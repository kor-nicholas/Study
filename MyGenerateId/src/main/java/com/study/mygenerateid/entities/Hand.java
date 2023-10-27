package com.study.mygenerateid.entities;

import org.springframework.stereotype.Component;

@Component
public class Hand {
    private String lifeLine;
    private int countFingers;

    public Hand() {
    }

    public Hand(String lifeLine, int countFingers) {
        this.lifeLine = lifeLine;
        this.countFingers = countFingers;
    }

    public String getLifeLine() {
        return lifeLine;
    }

    public int getCountFingers() {
        return countFingers;
    }

    @Override
    public String toString() {
        return "Hand{" +
                "lifeLine='" + lifeLine + '\'' +
                ", countFingers=" + countFingers +
                '}';
    }
}
