CREATE TABLE public.user (
 	user_id SERIAL PRIMARY KEY,
 	user_nick VARCHAR(64) NOT NULL UNIQUE
);

CREATE TABLE public.stocktype (
	stocktype_id SERIAL PRIMARY KEY,
	user_id INT,
 	stocktype_name VARCHAR(64) NOT NULL,
	UNIQUE(user_id, stocktype_name),
	CONSTRAINT fk_user
		FOREIGN KEY(user_id)
			REFERENCES public.user(user_id)
			ON DELETE CASCADE
);

CREATE TABLE public.stockform (
	stockform_id SERIAL PRIMARY KEY,
	user_id INT,
 	stockform_name VARCHAR(64) NOT NULL,
	UNIQUE(user_id, stockform_name),
	CONSTRAINT fk_user
		FOREIGN KEY(user_id)
			REFERENCES public.user(user_id)
			ON DELETE CASCADE
);



CREATE TABLE public.stocktype_stockform (
	stocktype_stockform_id SERIAL PRIMARY KEY,
 	stocktype_id INT,
	stockform_id INT,
	UNIQUE(stocktype_id, stockform_id),
	CONSTRAINT fk_stocktype
		FOREIGN KEY(stocktype_id)
			REFERENCES public.stocktype(stocktype_id)
			ON DELETE CASCADE,
	CONSTRAINT fk_stockform
		FOREIGN KEY(stockform_id)
			REFERENCES public.stockform(stockform_id)
			ON DELETE CASCADE
);

CREATE TABLE public.stockmaker (
	stockmaker_id SERIAL PRIMARY KEY,
	user_id INT,
 	stockmaker_name VARCHAR(64) NOT NULL,
	UNIQUE(user_id, stockmaker_name),
	CONSTRAINT fk_user
	FOREIGN KEY(user_id)
		REFERENCES public.user(user_id)
		ON DELETE CASCADE
);

CREATE TABLE public.stockproduct (
	stockproduct_id SERIAL PRIMARY KEY,
	user_id INT,
	stocktype_id INT,
	stockmaker_id INT,
 	stockproduct_name VARCHAR(64) NOT NULL,
	UNIQUE(user_id, stockmaker_id, stockproduct_name),
	CONSTRAINT fk_user
	FOREIGN KEY(user_id)
		REFERENCES public.user(user_id)
		ON DELETE CASCADE,
	CONSTRAINT fk_stocktype
	FOREIGN KEY(stocktype_id)
		REFERENCES public.stocktype(stocktype_id)
		ON DELETE CASCADE,
	CONSTRAINT fk_stockmaker
	FOREIGN KEY(stockmaker_id)
		REFERENCES public.stockmaker(stockmaker_id)
		ON DELETE NO ACTION
);

CREATE TABLE public.stock (
	stock_id SERIAL PRIMARY KEY,
	user_id INT NOT NULL,
	stockproduct_id INT NOT NULL,
	stock_expiration_date DATE,
 	stock_quantity NUMERIC(6, 1) NOT NULL,
	stock_notes VARCHAR(256),
	UNIQUE(user_id, stockproduct_id, stock_expiration_date),
	CONSTRAINT fk_user
	FOREIGN KEY(user_id)
		REFERENCES public.user(user_id)
		ON DELETE CASCADE,
	CONSTRAINT fk_stockproduct
	FOREIGN KEY(stockproduct_id)
		REFERENCES public.stockproduct(stockproduct_id)
		ON DELETE NO ACTION
);