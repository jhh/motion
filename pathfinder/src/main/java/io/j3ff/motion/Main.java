package io.j3ff.motion;

import com.squareup.moshi.JsonAdapter;
import com.squareup.moshi.Moshi;
import java.io.FileWriter;
import java.io.IOException;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVPrinter;

public class Main {

  public static void main(String[] args) {
    Moshi moshi = new Moshi.Builder().build();
    JsonAdapter<JupyterInput> jsonAdapter = moshi.adapter(JupyterInput.class);
    try {
      System.out.println("args = " + args[0]);
      JupyterInput jupyterInput = jsonAdapter.fromJson(args[0]);
      assert jupyterInput != null;
      if (jupyterInput.motion != null) {
        motion(jupyterInput.motion);
        return;
      }
      if (jupyterInput.pathfinder != null) {
        pathfinder(jupyterInput.pathfinder);
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  private static void motion(JupyterInput.MotionInput in) throws IOException {
    Motion motion = new Motion(in.dt, in.t1, in.t2, in.v_prog, in.dist);

    try (FileWriter out = new FileWriter("data/profile.csv")) {
      CSVPrinter printer =
          CSVFormat.DEFAULT.withHeader("Time", "Velocity", "Position", "Acceleration").print(out);
      while (!motion.isFinished()) {
        printer.printRecord(motion.calculate());
      }
    }
  }

  private static void pathfinder(JupyterInput.PathfinderInput in) throws IOException {
    Path path = new Path(in.toml);
    System.out.println(path);

    try (FileWriter out = new FileWriter("data/trajectory.csv")) {
      CSVPrinter printer =
          CSVFormat.DEFAULT
              .withHeader(
                  "dt", "x", "y", "position", "velocity", "acceleration", "jerk", "heading")
              .print(out);
      printer.printRecord(0, 0, 0, 0, 0, 0, 0, 0);
      printer.printRecords(path.calculate());
    }
  }
}
