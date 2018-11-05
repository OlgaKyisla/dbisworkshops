Для кожного завдання створити окремий файл назва.sql


--one-----------------------------
Insert into  Users_features (feature_name_fk, user_email_fk, user_attribute) values ('eyes','olha@gmail.com','black');

--------------------------------------------
--two------------------------
DELETE FROM makeup_features
WHERE
users_features.features_name_fk in 
    (
        SELECT
            users_features.features_name_fk
        FROM
            users_features
            JOIN feature ON users_features.feature_name_fk = feature.feature_name
            JOIN makeups_features ON makeups_features.feature_name_fk = feature.feature_name
    );

--three-------------------------------------------

update user 
set user_email = 'new@gmail.com'
where user.user_email  in 
(
SELECT
    user.user_email
FROM
    user
    JOIN users_features ON user.user_email = users_features.user_email_fk
    JOIN feature ON users_features.features_name_fk = feature.feature_name
    JOIN makeup_features ON makeups_features.feature_name_fk = feature.feature_name
    right JOIN makeup ON makeups_features.makeup_id_fk = makeup.makeup_id
where makeups_features.makeup_id_fk is null) ;
