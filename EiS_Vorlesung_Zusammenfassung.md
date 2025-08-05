Vorlesung 2: Python:

Daten + Variablen

Ausdrücke und Berechnungen

Befehle

Abstraktionen (Unterprogramme, Klassen, Komplexe Datentypen als Objekte, Polymorphie)

Systemumgebung

Statische Typisierung mit Python + MyPy + Typannotationen + Typchecks (also how does one annotate types in functions etc)

Typsysteme von Sprachen (statisch/dynamisch, stark/schwach typisiert)



Vorlesung 3: C/C++ (mostly as theoretical knowledge relevant for the exam, no programming exercises)

Daten + Variablen

Ausdrücke und Berechnungen

Befehle

Abstraktionen (Unterprogramme, Klassen, Komplexe Datentypen als Objekte, Polymorphie)

Systemumgebung

Zeiger

wichtige Sprachfeatures

Typisierung

Module + Bibliotheken (separate Übersetzung)

kurzer Vergleich mit JAVA/Python



Vorlesung 4: JAVA/Scala: (also more about core concepts than exercises)

Daten + Variablen

Ausdrücke und Berechnungen

Befehle

Abstraktionen (Unterprogramme, Klassen, Komplexe Datentypen als Objekte, Polymorphie)

Systemumgebung

Typisierung

Was ist JAVA, Vorteile/Nachteile

Was ist Scala, Vorteile/Nachteile

Module



Vorlesung 5: Der Softwareentwicklungsprozess: Probleme \& grobe Ansätze (this was mostly theoretical / felt like an introduction, doesnt seem relevant for the exam)

Ziele:

Funktion, Robustheit, Testbarkeit

Flexibilität, Erweiterbarkeit

Wiederverwendbarkeit

Verständlichkeit

Portabilität



Struktur eines Entwicklungsprozesses:

Aspekte der Softwareentwicklung

Prozedural, OOP, Funktional:

Ziel der Programmiertechniken

Abstraktionen (Modularisierung)



Vorlesung 6: Beispielprojekt: Vektorgraphik Editor

Aspekte des Projektes:

Vektorgraphik: Verschiedene Typen von Vektorobjekten, Verschiedene Attribute, Ausbau zu GUI Bibliothek

Interaktion (Manipulation mit der Maus)

Schritte (GUI Programmieren lernen mit Qt (oder AWT), Vektorgraphik Bibliothek prozedural, Implementation mit OOP (einfacher), GUI Elemente hinzufügen, Funktionale / Datenflussarchitektur)

Warum dieses Projekt?:

Komplexes Problem

Führt Design und Anwendung von GUIs mit ein

Historisch motivierend für OOP: Xerox Alto Projekt / Smalltalk / erstes moderne “ GUI

Vor und Nachteile von OOP \& FP Pattern gut sichtbar: Motivierend für moderne Ansätze

Relevant bis heute:

Interaktive Anwendungen, Webframeworks, Games

Fortgeschrittenes: Persistenz, automatische GUIs, etc.

Anforderungen:

Vektorgraphik:

Geometrische Primitive (z.B. Linien, Rechtecke, Kreise, Gruppierung)

Repräsentation als mathematische Beschreibung („Vektorgraphik“ (kein Auflösungslimit), Umwandung in Rastergraphik bei Bedarf)

Operationen (Erzeugen + Transformieren: verschieben)



In der Praxis: Wir nutzen eine 2D Graphikbibliothek (QPainter, Qt for Python), Vorgefertigte Kommandos für zeichnen, Zeichenflächen: Anwenden von QPainter auf QImage, QWidget

Berechnung Viewport „Viewport Transformation“, Ausschnitt verschieben

Orthogonale Anforderungen: Editieren mit der Maus (Erzeugen/Löschen, Transformieren), Editieren per Tastatur (Eigenschaften numerisch im UI setzen), Speichern und Laden

„Klassische“ Anwendung: Dokumentenorientiert, Drop Down Menüs für wesentliche Funktionen, Toolbars \& Shortcuts für schnellen Zugriff, "Inspector “ für numerisches Editieren

Erweiterbarkeit: Neue Primitive (Text, Sterne usw), Neue Werkzeuge zum Editieren, Dynamisches Laden von Plugins (Probleme bei Fehlerbehandlung lösen können dazu), Grundlegende / Unvorhergesehene Erweiterungen

Grobe Struktur: Komponenten:

Vektorgraphik Bibliothek, Editor

Wie packen wir es an?

Vektorgraphik Bibliothek: prozedurales Design, OOP Design, Dynamische Metaprogrammierung, funktionales Design

Editor: Interaktion strukturieren, Erweiterung zu allgemeinen GUIs



Vorlesung 7: Prozedurale Programmierung: Zwei Strukturelemente:

Funktionen / Prozeduren

Datentypen

Datentypen u. Produkttypen: Theorie

Produkttypen in Python

Traditionelle Klassen in Python, Dataclasses, Arrays

Summentypen: Implementation, Typprüfung

Summentypen in Python

Entwurfstechniken

Datenflussdiagramme (DFDs) + Vorgehen

Graphischer Entwurf von Datentypen (UML „Klassendiagramme“)

Entwurf Vektorgraphik Bibliothek (Zeichenalgorithmus)

Entwurfsprinzip: „Bäume“ von Objekten, Abstrakte Datentypen (Welche Operationen braucht man)

Unterprogramme

Objektorientiertes Design



Vorlesung 8: Objekt-Orientierte Programmierung:

Funktionale Programmierung (Idee, Funktionale Abstraktionen)

Objektorientierte Programmierung (Ideen: Abstrakte Datentypen, Polymorphie, Vererbung)

ADTs (Abstrakte Datentypen) in OOP

Subtyping durch Vererbung

Vererbung

Subtyping vs. Sum Types

Vorteile und Nachteile Vererbung

Abstrakte Klassen

OOP in Scala vs. Python

Objekt Orientierter Entwurf (Kernkonzepte: Klassen, Methoden) + Entwurfsstrategie (Klassen finden / Vererbungshierarchien identifizieren, Oberklassen formulieren), Wann Vererbung benutzen? Worauf achten? Wie entwirft man Oberklassen?

UML Diagramme: Wie entwirft man Software? Struktur: Klassendiagramme, Beziehungen zwischen Klassen, Unterschiedliche Zusammensetzung, Multiplizitäten, Rollenbezeichnungen, Interfaces

Bitmapbilder

Type Checking, Virtuelle Methodentabellen



Vorlesung 9: GUIs: Graphische Benutzerschnittstellen

Widgets als Oberklasse, Labels, Baum von Widgets, Widget Hierarchie: Objektbaum, Gui Frameworks (schematisch), Eventbehandlung

Event-Queues/Loops (Ereignisorientierte Architektur), Design Patterns, Ereignisse im Widget-Baum, im Bsp. Qt in Python

Entwurf von Benutzerschnittstellen, Ansätze, Leitlinien, Heuristiken



Vorlesung 10: Funktionale Programmierung

Grundidee, Prinzipien

Funktionen, Typisierung, Funktionen als Bausteine, Higher Order Functions, Allgemeine Leitlinien, Entwurfsstrategien

Datenflussgraph:Architektur

„Erweiterbarkeit“ OOP vs Functional

Techniken speziell für Functional programming: Algebraic Data Types + Pattern Matching, Data Flow Architectures, Caching (Tesselierung?), z.B. für DFGs, Unbenannte Funktionen („Lambda Expressions"), Closures (Variablenbindung an Funktionskontext), Partial Application \& Currying, Lazy Evaluation, Continuations 



Vorlesung 11: Hardwarenahe Programmierung (seems less relevant, wasnt included that much in the exercises)

Low Level Programmierung: Performance + Abstraktionstechniken

Ziele:Programmiertechniken, Abstraktionsmechanismen, Übersichtsartig, Details nicht wesentlich, Programmieren einfacher, schneller Datenverarbeitung in C++ (not klausurrelevant because no programming exercises in C++)



Vorlesung 12: Parallele Programmierung (seems less relevant, wasnt included that much in the exercises)

Technischer Hintergrund: Parallele Architekturen, Parallele Herausforderungen (Deadlocks, Race Conditions), Synchronisationsprimitive, Architekturmuster

Wie funktioniert es?(Verteiltes System, Shared Memory, Präemptives MultiTasking, Kooperatives MultiTasking)

MultiTasking: Begriffe (Präemptiv / MultiCore / Multi CPU)

(Client-)Server-Pattern (Eigenschaften, Beliebtes Muster, Entwurfsprinzipien) 

Vorteile Server

Nebenläufigkeit in Programmiersprachen (Python, C++)

Sockets: Message Queues für das Internet (Verteilte Systeme, TCP/IP vs. UDP/IP, Server Architektur, Standard Client/Server Architektur)



Vorlesung 13: Fortgeschrittene Programmiertechniken (seems less relevant, wasnt included much or at all in the exercises)

Standard OOP Design:

Objekthierarchien, Serialisierung (und dynamische Metaprogrammierung) und Infrastruktur

Speichern Prozedural

„Serialisierung“ an Bsp. Objektorientiert (Schreiben eines „Shapes“, Schreiben einer Liste wie „Group“), Aufteilung (+Vorteile) (Stream-Klasse statt unstrukturierte Dateien, Shape Objekte

Weitere Herausforderungen (Änderungen / Maßnahmen, Zyklische Graphen von Objekten, Abhilfe)

Reflection Introspection (Objekte + Probleme : Lösung = Dynamische Meta-Programmierung via Reflektion) 

Struktur (Python, JAVA/Scala, C++) von Meta-Klassen, Was muss eine (Laufzeitrepräsentation) einer Klasse können?

Reflection in Python: Automatische Serialisierung (Methoden write/read, Standardbibliotheken)

Nachteile (Versionierung, Sicherheitsrisiken) + was stattdessen?

Was kann man noch alles mit Reflection machen?

Advanced Reflection (Reflektion als allgemeines Prinzip, Beispiele)

MVC: Model · View · Controller: MVC \& „MP“, Funktional oder Imperativ?, Wie setze ich das um?

„Command Object“ Architekturen (Zwei Probleme: GUI vs. Konsole, x2 Featurewünsche)

(F)RP- (Functional-) Reactive Programming + Im GUI Kontext

Techniken für Modularisierung erweiterbare Software

Polymorphie: Fortgeschrittene Methoden \& Konzepte (Arten von Polymorphie - + in Python, C++/JAVA/Scala), Subtyping, Generische Typen, Allgemeines Prinzip, Typparameter, Generische Klassen, Co-, Contra-, und Invarianz









