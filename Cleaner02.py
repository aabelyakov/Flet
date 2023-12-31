import flet
from flet import *
from flet import icons, colors


def main(page: Page):
    page.bgcolor = "lightblue"
    page.scroll = True

    page.add(
        AppBar(
            bgcolor="lightblue",
            leading=IconButton(
                icon=icons.ARROW_BACK_IOS),

            title=Text("App Cleaner", color="white",
                       weight="bold"
                       ),
            actions=[
                IconButton(
                    icon=icons.YOUTUBE_SEARCHED_FOR,
                    icon_color=colors.BLACK,
                    icon_size=30
                ),
                IconButton(
                    icon=icons.STAR_RATE,
                    icon_color=colors.BLACK,
                    icon_size=30
                )
            ]
        ),
        # END APPBAR
        # THIS BODY SECTION
        Column([
            Row([
                Card(
                    elevation=20,
                    content=Container(
                        padding=20,
                        height=120,
                        width=270,
                        border_radius=border_radius.only(
                            topRight=30,
                            bottomLeft=30
                        ),
                        content=Column([
                            Row([
                                Text("1.31 GB", weight="bold", size=30),
                            ], alignment="center"),
                            Row([
                                Text("Cleanup Sugested",
                                     color="#87888A",
                                     size=10
                                )
                            ],
                                alignment="center")
                        ], alignment="center")
                        # END CONTAINER
                    )
                )
            ], alignment="center"),
            # PROGRESSBAR SECTION
            Row([
                ProgressBar(width=300, value=0.4)
            ], alignment="center"),

            # ICON INFO SECTION
            Row([
                Container(
                    content=Row([
                        Icon(icons.THUMB_UP, size=20, color="black"),
                        Text("Used 3.2 Gb", size=15, color="black",weight="bold")
                    ], alignment="center")
                ),
                Container(
                    content=Row([
                        Icon(icons.EMOJI_OBJECTS, size=20, color="black"),
                        Text("Deleted 31 Gb",
                             size=15,
                             color="black",
                             weight="bold"
                        )
                    ], alignment="center")
                ),
            ], alignment="center"),

            # SECTION NEW DETAILS

            Column([
                Container(
                    padding=20,
                    margin=margin.symmetric(vertical=30),
                    bgcolor="black",
                    border_radius=border_radius.only(
                        topRight=30,
                        bottomRight=30
                    ),
                    content=Text(
                        "can be Deleted",
                        size=20,
                        weight="bold",
                        color="white"
                    )
                ),
                # STACK CARD
                Stack([
                    Card(
                        elevation=30,
                        content=Container(
                            # FULL SCREEN WIDTH
                            width=page.window_width,
                            margin=margin.only(top=-10),
                            height=300,
                            content=Column([
                                ListTile(
                                    leading=Icon(icons.ADD_REACTION),
                                    title=Text("Junk Files",
                                               color="black", size=20,
                                               weight="bold",
                                               ),
                                    subtitle=Row([
                                        Icon(name="group_off",
                                             color="red",
                                             size=15
                                             ),
                                        Text("1.15 Gb Found",
                                             size=15,
                                             color="grey"
                                             )
                                    ])
                                ),
                                ListTile(
                                    leading=Icon(icons.ADD_REACTION),
                                    title=Text("Trash File",
                                               color="red", size=20,
                                               weight="bold"
                                               ),
                                    trailing=ElevatedButton(
                                        "Let Cleaned",
                                        icon=icons.WHATSHOT,
                                        color="green",
                                        icon_color="green"
                                    ),
                                    subtitle=Row([
                                        Icon(name="group_off",
                                             color="red", size=15),
                                        Text("1.15 Gb Found",
                                             size=15,
                                             color="grey"
                                             )
                                    ])
                                ),
                                ListTile(
                                    leading=Icon(icons.ADD_REACTION),
                                    title=Text("Slow Performance",
                                               color="orange", size=20,
                                               weight="bold"
                                               ),
                                    subtitle=Row([
                                        Icon(name="group_off",
                                             color="red", size=15),
                                        Text("1.15 Gb Found",
                                             size=15,
                                             color="grey"
                                             )
                                    ])
                                ),

                            ])
                        )
                    ),
                    Row([
                        Card(
                            elevation=20,
                            content=Container(
                                margin=margin.symmetric(vertical=-30),
                                border_radius=border_radius.only(
                                    bottomLeft=30, topRight=30),
                                padding=10,
                                bgcolor="green",
                                content=Row([
                                    Icon(icons.FAVORITE, color=colors.PINK),
                                    Text("Health System", size=20,
                                         weight="bold",
                                         color="white"
                                         )
                                ])
                            )
                        )

                    ], alignment="end")
                    # END STACK
                ]),
                # NEW FINAL SECTION
                Row([
                    Container(
                        # FOR RIPPLE EFECT IN CONTAINER
                        ink=True,
                        padding=10,
                        border_radius=border_radius.all(30),
                        border=border.all(5, color="white"),
                        on_click=lambda e: print("hello test"),
                        content=Row([
                            Icon(icons.TOUCH_APP, size=30, color="white"),
                            Text("Optimize Now", color="white", size=30)
                        ])
                    )

                ], alignment="center")

            ])
        ], spacing=0)
    )


flet.app(target=main)
