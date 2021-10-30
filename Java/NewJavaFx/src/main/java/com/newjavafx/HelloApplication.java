package com.newjavafx;

import javafx.application.*;
import javafx.geometry.*;
import javafx.scene.*;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.*;

import java.io.IOException;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        stage.setTitle("My New Javafx App");
        stage.setWidth(300);
        stage.setHeight(300);

        Button bt = new Button("Save");
        Button bt2 = new Button("Cancel");

        Label lb = new Label("Click there to Save");
        Label lb2 = new Label("Click there to Cancel");

        VBox vb = new VBox();
        VBox vb2 = new VBox();
        HBox hb = new HBox();

        vb.getChildren().addAll(lb, bt);
        vb.setAlignment(Pos.BOTTOM_CENTER);
        vb.setSpacing(10);

        vb2.getChildren().addAll(lb2, bt2);
        vb2.setAlignment(Pos.BOTTOM_CENTER);
        vb2.setSpacing(10);

        hb.getChildren().addAll(vb, vb2);
        hb.setSpacing(5);
        hb.setAlignment(Pos.BOTTOM_CENTER);

        Scene sc = new Scene(hb);
        stage.setScene(sc);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}