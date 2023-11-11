#include "mainwindow.h"
//#include "custombutton.h"
#include <QPropertyAnimation>


MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), isMenuExpanded(false)
{
    // Hamburger button setup
    hamburgerButton = new QPushButton();
    hamburgerButton->setIcon(QIcon(":/icons/burger.png")); // Start with the burger icon
    hamburgerButton->setFixedSize(40, 40); // Set your desired size
    connect(hamburgerButton, &QPushButton::clicked, this, &MainWindow::toggleMenu);

    // Fixed position layout for hamburger button
    QVBoxLayout *fixedButtonLayout = new QVBoxLayout;
    fixedButtonLayout->addWidget(hamburgerButton);
    fixedButtonLayout->addStretch(); // This will push the hamburger button to the top
    fixedButtonLayout->setAlignment(Qt::AlignTop); // Align to top-left

    // Menu buttons setup
    QPushButton *mainPageButton = new QPushButton("Main Page");
    QPushButton *accountInfoButton = new QPushButton("Account Info");
    QPushButton *tradingButton = new QPushButton("Trading");
    QPushButton *marketInfoButton = new QPushButton("Market Info");

    // Connect menu buttons to their respective slots
    connect(mainPageButton, &QPushButton::clicked, this, &MainWindow::showMainPage);
    connect(accountInfoButton, &QPushButton::clicked, this, &MainWindow::showAccountInfoPage);
    connect(tradingButton, &QPushButton::clicked, this, &MainWindow::showTradingPage);
    connect(marketInfoButton, &QPushButton::clicked, this, &MainWindow::showMarketInfoPage);

    // Menu layout setup
    menuLayout = new QVBoxLayout;
    menuLayout->addWidget(mainPageButton);
    menuLayout->addWidget(accountInfoButton);
    menuLayout->addWidget(tradingButton);
    menuLayout->addWidget(marketInfoButton);
    menuLayout->setAlignment(Qt::AlignTop); // Ensure alignment to the top

    // Main sidebar layout that combines the fixed button layout and the menu layout
    QVBoxLayout *sidebarLayout = new QVBoxLayout;
    sidebarLayout->addLayout(fixedButtonLayout); // Add fixed button layout first
    sidebarLayout->addLayout(menuLayout);        // Then add the menu layout

    // Pages setup
    pagesWidget = new QStackedWidget;
    mainPage = new QWidget; // Replace with your custom widget or layout
    accountInfoPage = new QWidget; // Replace with your custom widget or layout
    tradingPage = new QWidget; // Replace with your custom widget or layout
    marketInfoPage = new QWidget; // Replace with your custom widget or layout
    pagesWidget->addWidget(mainPage);
    pagesWidget->addWidget(accountInfoPage);
    pagesWidget->addWidget(tradingPage);
    pagesWidget->addWidget(marketInfoPage);

    // Sidebar widget setup
    QWidget *sidebarWidget = new QWidget;
    sidebarWidget->setLayout(sidebarLayout);

    // Initialize sidebar animation
    sidebarAnimation = new QPropertyAnimation(sidebarWidget, "maximumWidth");
    sidebarAnimation->setDuration(500); // Set the duration of the animation

    // Main horizontal layout
    QHBoxLayout *mainLayout = new QHBoxLayout;
    mainLayout->addWidget(sidebarWidget); // Sidebar widget
    mainLayout->addWidget(pagesWidget, 1); // Pages widget takes up the rest of the space


    // Set the central widget
    QWidget *centralWidget = new QWidget;
    centralWidget->setLayout(mainLayout);
    setCentralWidget(centralWidget);

    // Ensure the menu starts hidden if isMenuExpanded is false
    toggleMenu(); // Call this once to set the initial visibility state
}

//void MainWindow::toggleMenu() {
//    // Toggle the expanded state
//    isMenuExpanded = !isMenuExpanded;

//    // Show or hide the menu buttons
//    for (int i = 0; i < menuLayout->count(); ++i) { // Iterate over menu items
//        QWidget *widget = menuLayout->itemAt(i)->widget();
//        if (widget) {
//            widget->setVisible(isMenuExpanded);
//        }
//    }

//    // Update the icon based on the state
//    QIcon icon = isMenuExpanded ? QIcon(":/icons/arrow.png") : QIcon(":/icons/burger.png");
//    hamburgerButton->setIcon(icon);
//    hamburgerButton->setIconSize(QSize(20, 20)); // Keep icon size consistent
//}


void MainWindow::toggleMenu() {
    QWidget *sidebarWidget = menuLayout->parentWidget();
    int startWidth = sidebarWidget->maximumWidth();
    int endWidth;

    if (isMenuExpanded) {
        // If the menu is expanded, shrink it
        endWidth = 50; // Minimal width when shrunk
    } else {
        // If the menu is collapsed, expand it
        endWidth = 200; // Full width when expanded
    }

    // Set animation start and end values
    sidebarAnimation->setStartValue(startWidth);
    sidebarAnimation->setEndValue(endWidth);

    // Start the animation
    sidebarAnimation->start();

    // Toggle the expanded state
    isMenuExpanded = !isMenuExpanded;
}


void MainWindow::showMainPage() {
    pagesWidget->setCurrentWidget(mainPage);
}

void MainWindow::showAccountInfoPage() {
    pagesWidget->setCurrentWidget(accountInfoPage);
}

void MainWindow::showTradingPage() {
    pagesWidget->setCurrentWidget(tradingPage);
}

void MainWindow::showMarketInfoPage() {
    pagesWidget->setCurrentWidget(marketInfoPage);
}

MainWindow::~MainWindow() {
    // Cleanup if necessary
}
