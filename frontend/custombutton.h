#ifndef CUSTOMBUTTON_H
#define CUSTOMBUTTON_H

#include <QPushButton>
#include <QPainter>

class CustomButton : public QPushButton {
    Q_OBJECT // This macro is required to use signals and slots

public:
    CustomButton(QWidget *parent = nullptr);

protected:
    void paintEvent(QPaintEvent *event) override;

private:
    bool toggledState = false; // Changed variable name to avoid confusion with the signal

signals:
    void toggled(); // Define the signal here

public slots:
    void toggleButton(); // Slot that will be called when the button is clicked
};

#endif // CUSTOMBUTTON_H
