INSERT INTO public.user (user_nick) VALUES ('halogenki');

INSERT INTO
	public.stocktype(user_id, stocktype_name)
VALUES
		(1, 'COL_PAP'),
		(1, 'DIR_POS_PAP'),
		(1, 'BW_RC_PAP'),
		(1, 'BW_FB_PAP'),
		(1, 'INST_PAP'),
		(1, 'BW_NEG'),
		(1, 'BW_REV'),
		(1, 'COL_NEG'),
		(1, 'COL_REV'),
		(1, 'BW_DEV'),
		(1, 'BW_FIX'),
		(1, 'STOP'),
		(1, 'TONER'),
		(1, 'HELPER'),
		(1, 'C41'),
		(1, 'E6'),
		(1, 'RA4');

INSERT INTO
	public.stockform(user_id, stockform_name)
VALUES
		(1, 'PAP_ROLL'),
		(1, 'PAP_SHEET'),
		(1, 'FILM_CART'),
		(1, 'FILM_ROLL'),
		(1, 'FILM_BULK'),
		(1, 'FILM_SHEET'),
		(1, 'CH_LIQ'),
		(1, 'CH_POW'),
		(1, 'CH_PACK');

INSERT INTO
	public.stocktype_stockform(stocktype_id, stockform_id)
VALUES
		(1, 1),
		(1, 2),
		(2, 1),
		(2, 2),
		(3, 1),
		(3, 2),
		(4, 1),
		(4, 2),
		(5, 3),
		(6, 3),
		(6, 4),
		(6, 5),
		(6, 6),
		(7, 3),
		(7, 4),
		(7, 5),
		(7, 6),
		(8, 3),
		(8, 4),
		(8, 5),
		(8, 6),
		(9, 3),
		(9, 4),
		(9, 5),
		(9, 6),
		(10, 7),
		(10, 8),
		(10, 9),
		(11, 7),
		(11, 8),
		(11, 9),
		(12, 7),
		(12, 8),
		(12, 9),
		(13, 7),
		(13, 8),
		(13, 9),
		(14, 7),
		(14, 8),
		(14, 9),
		(15, 7),
		(15, 8),
		(15, 9),
		(16, 7),
		(16, 8),
		(16, 9),
		(17, 7),
		(17, 8),
		(17, 9);

INSERT INTO public.stockmaker(user_id, stockmaker_name)
VALUES
	(1, 'AGFAPHOTO'),
	(1, 'FOMA'),
	(1, 'FUJI'),
	(1, 'ILFORD'),
	(1, 'TETENAL'),
	(1, 'KODAK');

INSERT INTO public.stockproduct(user_id, stocktype_id, stockmaker_id, stockproduct_name)
VALUES (1, 3, 2, 'FOMASPEED VARIANT 311 10x15');