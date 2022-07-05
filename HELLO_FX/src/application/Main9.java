package application;



import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.Dialog;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class Main9 extends Application {
	TextField tf;
	Button btn0,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btnCall;
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox) FXMLLoader.load(getClass().getResource("main9.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			btn0 = (Button) scene.lookup("#btn0");
			btn1 = (Button) scene.lookup("#btn1");
			btn2 = (Button) scene.lookup("#btn2");
			btn3 = (Button) scene.lookup("#btn3");
			btn4 = (Button) scene.lookup("#btn4");
			
			btn5 = (Button) scene.lookup("#btn5");
			btn6 = (Button) scene.lookup("#btn6");
			btn7 = (Button) scene.lookup("#btn7");
			btn8 = (Button) scene.lookup("#btn8");
			btn9 = (Button) scene.lookup("#btn9");
			
			btnCall = (Button) scene.lookup("#btn_call");
			
			tf = (TextField) scene.lookup("#tf");
			tf.setAlignment(Pos.CENTER_RIGHT); //scenebuilder 스타일에서도 설정가능
			
			btn0.setOnMouseClicked(new EventHandler<Event>(){
				@Override
				public void handle(Event event) {
				Button imsi = (Button) event.getSource();
				imsi.getText();
					tf.appendText("0");
				}
				
			});
			
			btn1.setOnMouseClicked(new EventHandler<Event>(){
				@Override
				public void handle(Event event) {
					tf.appendText("1");
				}
				
			});
			
			btn2.setOnMouseClicked(new EventHandler<Event>(){
				@Override
				public void handle(Event event) {
					tf.appendText("2");
				}
				
			});
			
			btn3.setOnMouseClicked(new EventHandler<Event>(){
				@Override
				public void handle(Event event) {
					tf.appendText("3");
				}
				
			});
			
			btn4.setOnMouseClicked(new EventHandler<Event>(){
				@Override
				public void handle(Event event) {
					tf.appendText("4");
				}
				
			});
			
			btn5.setOnMouseClicked(new EventHandler<Event>(){
				@Override
				public void handle(Event event) {
					tf.appendText("5");
				}
				
			});
			
			btn6.setOnMouseClicked(new EventHandler<Event>(){
				@Override
				public void handle(Event event) {
					tf.appendText("6");
				}
				
			});
			
			btn7.setOnMouseClicked(new EventHandler<Event>(){
				@Override
				public void handle(Event event) {
					tf.appendText("7");
				}
				
			});
			
			btn8.setOnMouseClicked(new EventHandler<Event>(){
				@Override
				public void handle(Event event) {
					tf.appendText("8");
				}
				
			});
			
			btn9.setOnMouseClicked(new EventHandler<Event>(){
				@Override
				public void handle(Event event) {
					tf.appendText("9");
				}
				
			});
			
			btnCall.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myClick();
				}
			});

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public void myClick() {
		Alert alert = new Alert(AlertType.INFORMATION);
		alert.setTitle("전화걸기");
		String telNum = tf.getText();
		alert.setHeaderText("calling " + telNum);
		alert.show();
	}

	public static void main(String[] args) {
		launch(args);
	}

}
