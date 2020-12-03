--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-05-08 07:52:45



--
-- TOC entry 204 (class 1259 OID 16731)
-- Name: attendee; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.attendee (
    id integer NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    conference_id integer NOT NULL,
    job_position text NOT NULL,
    email text NOT NULL,
    company text NOT NULL,
    city text NOT NULL,
    state text NOT NULL,
    interests text,
    submitted_date timestamp with time zone NOT NULL,
    comments text
);


--
-- TOC entry 205 (class 1259 OID 16744)
-- Name: attendee_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.attendee ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.attendee_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 202 (class 1259 OID 16722)
-- Name: conference; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.conference (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    active bit(1) NOT NULL,
    date date NOT NULL,
    price double precision NOT NULL,
    address character varying(300) NOT NULL
);


--
-- TOC entry 203 (class 1259 OID 16729)
-- Name: conference_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.conference ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.conference_id_seq
    START WITH 1
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 99999
    CACHE 1
);


--
-- TOC entry 206 (class 1259 OID 16746)
-- Name: notification; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.notification (
    id integer NOT NULL,
    status text NOT NULL,
    message text NOT NULL,
    submitted_date timestamp with time zone,
    completed_date timestamp with time zone,
    subject text NOT NULL
);


--
-- TOC entry 207 (class 1259 OID 16754)
-- Name: notification_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.notification ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.notification_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 2836 (class 0 OID 16731)
-- Dependencies: 204
-- Data for Name: attendee; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.attendee (first_name, last_name, conference_id, job_position, email, company, city, state, interests, submitted_date, comments)
VALUES
('Lanice', 'Montre',	1, 'Director', 'lamontre@gmail.com', 'Montreal Consulting Inc', 'Philadelphia', 'PA', 'ML', '2020-05-07 00:00:00-04', 'learn more'),
('Do', 'Ji',	1, 'Director', 'mar@smith.org', 'Mafolab', 'Rockville', 'AZ', 'CC', '2020-05-07 00:00:00-04', 'networking'),
( 'Edem', 'Lamoine',	1, 'Executive', 'lamoine@gmail.com', 'Paracetamole Pharma', 'Washington', 'DC', 'DS', '2020-05-07 00:00:00-04', 'Hands on experience'),
( 'Celine', 'Mabs',	1, 'Developer', 'celinemabs@school.edu', 'Mabs Learning Center', 'Rawlings', 'WY', 'DS', '2020-05-07 00:00:00-04', 'Hand-ons experience and networking with engineers in the field'),
( 'Mary', 'Maine',	1, 'Other', 'mary.maine@noreply.com', 'Maine Co', 'Hanover', 'PA', 'ML', '2020-05-07 00:00:00-04', 'Looking forward to start the class');


--
-- TOC entry 2834 (class 0 OID 16722)
-- Dependencies: 202
-- Data for Name: conference; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.conference (name, active, date, price, address)
VALUES
('TechConf', B'1', '2022-06-10', 495, '123 Main St, Baltimore, MD 12345'),
('TestConf', B'0', '1999-01-01', 1, '9');



--
-- TOC entry 2838 (class 0 OID 16746)
-- Dependencies: 206
-- Data for Name: notification; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.notification (status, message, submitted_date, completed_date, subject)
VALUES
('Notifications submitted',' ', NULL, NULL, ''),
('Notifications submitted','uyt','2020-05-07 18:00:38.573856-04','2020-05-07 18:00:39.124435-04','Welcome Email'),
('Notified 5 attendees','Welcome Email','2020-05-07 18:14:04.239065-04','2020-05-07 18:14:04.271981-04','Welcome Email'),
('Notifications submitted','New Speaker Added: Dr Daniel Shu','2020-05-07 23:24:00.504412-04', NULL,'New Speaker Added: Dr Daniel Shu');




--
-- TOC entry 2704 (class 2606 OID 16738)
-- Name: attendee attendee_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.attendee
    ADD CONSTRAINT attendee_pkey PRIMARY KEY (id);


--
-- TOC entry 2702 (class 2606 OID 16726)
-- Name: conference conference_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.conference
    ADD CONSTRAINT conference_pkey PRIMARY KEY (id);


--
-- TOC entry 2706 (class 2606 OID 16753)
-- Name: notification notification_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.notification
    ADD CONSTRAINT notification_pkey PRIMARY KEY (id);


--
-- TOC entry 2707 (class 2606 OID 16739)
-- Name: attendee conference; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.attendee
    ADD CONSTRAINT conference FOREIGN KEY (conference_id) REFERENCES public.conference(id);


-- Completed on 2020-05-08 07:52:45

--
-- PostgreSQL database dump complete
--

