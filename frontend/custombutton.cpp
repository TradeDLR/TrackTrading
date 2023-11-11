#include "CustomButton.h"
#include <QPainter>
#include <QPainterPath> // Include QPainterPath header

CustomButton::CustomButton(QWidget *parent) : QPushButton(parent) {
    connect(this, &QPushButton::clicked, this, &CustomButton::toggleButton);
}

void CustomButton::paintEvent(QPaintEvent *event) {
    QPushButton::paintEvent(event);

    QPainter painter(this);
    painter.setPen(Qt::NoPen);
    painter.setBrush(Qt::black);

    int lineThickness = height() / 10;
    int lineLength = width() - 20; // Assuming some padding
    int lineSpacing = lineThickness * 1.5;

    // Draw three lines for hamburger or "X" for toggled
    if (!toggledState) {
        // Hamburger
        for (int i = 0; i < 3; ++i) {
            QRect lineRect(10, (height() / 2 - lineThickness / 2) - lineSpacing + i * lineSpacing, lineLength, lineThickness);
            painter.drawRect(lineRect);
        }
    } else {
        // "X" shape
        QPainterPath path;
        path.moveTo(10, 10);
        path.lineTo(width() - 10, height() - 10);
        path.moveTo(10, height() - 10);
        path.lineTo(width() - 10, 10);
        painter.setPen(QPen(Qt::black, lineThickness));
        painter.drawPath(path);
    }
}

void CustomButton::toggleButton() {
    toggledState = !toggledState;
    emit toggled(); // Emit your custom signal
    update(); // Call update to trigger a repaint
}

