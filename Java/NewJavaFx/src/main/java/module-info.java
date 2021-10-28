module com.newjavafx {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.graphics;


    opens com.newjavafx to javafx.fxml;
    exports com.newjavafx;
}