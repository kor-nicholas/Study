/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab5;

/**
 *
 * @author ProBook
 */
public class ListObject {
        private String str;
        private short sh;
        
        ListObject() {
            this.sh = 1;
            this.str = "default";
        }
        
        ListObject(String str) {
            this.sh = 1;
            this.str = str;
        }
        
        ListObject(short sh) {
            this.sh = sh;
            this.str = "default";
        }
        
        ListObject (String str, short sh) {
            this.sh = sh;
            this.str = str;
        } 
        
        public void setStr(String str) {
            this.str = str;
        }
        
        public String getStr() {
            return str;
        }
        
        public short getSh() {
            return sh;
        }

        @Override
        public String toString() {
            return "ListObject{" + "str=" + str + ", sh=" + sh + '}';
        }
    }
