package com.narradoriamx;

import android.app.Activity;
import android.os.Bundle;
import android.graphics.Color;
import android.graphics.Typeface;
import android.view.Gravity;
import android.widget.*;

public class MainActivity extends Activity {

    private TextView status;
    private boolean active = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setGravity(Gravity.CENTER_HORIZONTAL);
        root.setPadding(28, 40, 28, 28);
        root.setBackgroundColor(Color.rgb(16, 24, 32));

        TextView title = new TextView(this);
        title.setText("NARRADOR IA MX");
        title.setTextColor(Color.WHITE);
        title.setTextSize(28);
        title.setTypeface(null, Typeface.BOLD);
        root.addView(title);

        TextView subtitle = new TextView(this);
        subtitle.setText("Tu partido. Tu transmisión. Dos voces.");
        subtitle.setTextColor(Color.LTGRAY);
        subtitle.setTextSize(15);
        root.addView(subtitle);

        addCommentator(root, "NARRADOR 1", "Relato principal");
        addCommentator(root, "NARRADOR 2", "Analista de partido");

        status = new TextView(this);
        status.setText("Sistema listo para iniciar");
        status.setTextColor(Color.rgb(0, 208, 132));
        status.setTextSize(16);
        status.setGravity(Gravity.CENTER);
        status.setPadding(0, 35, 0, 20);
        root.addView(status);

        Button start = new Button(this);
        start.setText("INICIAR NARRACIÓN DE PRUEBA");
        start.setOnClickListener(v -> {
            active = !active;
            status.setText(active
                ? "Narración de prueba activada"
                : "Narración de prueba detenida");
            start.setText(active ? "DETENER PRUEBA" : "INICIAR NARRACIÓN DE PRUEBA");
        });
        root.addView(start);

        setContentView(root);
    }

    private void addCommentator(LinearLayout root, String name, String role) {
        TextView card = new TextView(this);
        card.setText(name + "\n" + role);
        card.setTextColor(Color.WHITE);
        card.setTextSize(18);
        card.setPadding(20, 25, 20, 25);
        card.setBackgroundColor(Color.rgb(31, 45, 56));

        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(-1, -2);
        params.setMargins(0, 20, 0, 0);
        root.addView(card, params);
    }
}
