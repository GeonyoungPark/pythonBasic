package application;



import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class MainA extends Application {
	TextField tf1,tf2,tf3,tf4;
	@Override
	public void start(Stage primaryStage) {
		try {

			VBox root = (VBox) FXMLLoader.load(getClass().getResource("mainA.fxml"));
			Scene scene = new Scene(root, 400, 400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			Button btn = (Button) scene.lookup("#btn");
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			tf3 = (TextField) scene.lookup("#tf3");
			tf4 = (TextField) scene.lookup("#tf4");
		
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

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
		int sum = 0;
		int firstNum = Integer.parseInt(tf1.getText());
		int secondNum = Integer.parseInt(tf2.getText());
		int thirdNum = Integer.parseInt(tf3.getText());
		for (int i = firstNum; i <= secondNum; i++) {
			if ((i % thirdNum) == 0) {
				sum += i;
			}
		}
		tf4.setText(sum+"");
	}

	public static void main(String[] args) {
		launch(args);
	}

}
