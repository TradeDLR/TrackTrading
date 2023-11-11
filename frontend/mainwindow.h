#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QPushButton>
#include <QStackedWidget>
#include <QVBoxLayout>
#include <QPropertyAnimation>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void toggleMenu();
    void showMainPage();
    void showAccountInfoPage();
    void showTradingPage();
    void showMarketInfoPage();

private:
    QPushButton *hamburgerButton;
    QVBoxLayout *menuLayout;
    QStackedWidget *pagesWidget;

    QWidget *mainPage;
    QWidget *accountInfoPage;
    QWidget *tradingPage;
    QWidget *marketInfoPage;
    QPropertyAnimation *sidebarAnimation;

    bool isMenuExpanded;
};

#endif // MAINWINDOW_H
