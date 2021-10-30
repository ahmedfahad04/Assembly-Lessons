package com.newjavafx;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.layout.*;
import javafx.stage.*;
import javafx.scene.control.*;


public class GridLayout extends Application {

    public void start(Stage primaryStage){

        // layout
        GridPane gp = new GridPane();

        // adding nodes to the layout (col, row)
        int row = 0;

        for(int i=0; i<9; ){

            // node
            Button bt = new Button();
            bt.setMaxSize(20,20);
            
            // adding label to the node
            StringBuffer sb = new StringBuffer();
            sb.append(i+1);
            bt.setText(String.valueOf(sb));

            // adding nodes to the layout
            gp.add(bt, i%3,row);
            i++;

            // incrementing col count
            if (i%3==0){
                row+=1;
            }
        }

        gp.setAlignment(Pos.CENTER);
        gp.setHgap(10.0);
        gp.setVgap(10.0);

        // adding the layout to the scene
        Scene sc = new Scene(gp);

        // adding the scene to the window(Stage)
        primaryStage.setScene(sc);
        primaryStage.setTitle("Grid Pane Demonstration");
        primaryStage.setWidth(300);
        primaryStage.setHeight(300);
        primaryStage.show();

    }
}
