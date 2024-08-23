
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, Button, Typography } from '@mui/material';
import { makeStyles } from '@mui/styles';
import image from "./bg.png";

const useStyles = makeStyles(() => ({
  mainContainer: {
    backgroundImage: `url(${image})`,
    backgroundRepeat: 'no-repeat',
    backgroundPosition: 'center',
    backgroundSize: 'cover',
    height: "100vh",
    object_fit:'cover',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
  },
  appbar: {
    background: '#be6a77',
    boxShadow: 'none',
    color: 'white'
  },
  content: {
    textAlign: 'center',
    color: 'white',
  },
  button: {
    margin: '10px',
    padding: '15px 30px',
    fontSize: '18px',
  },
}));

const SelectPrediction = ({ setPredictionType }) => {
  const classes = useStyles();
  const navigate = useNavigate();

  const handleSelection = (type) => {
    setPredictionType(type);
    navigate(`/${type}_predict`);
  };

  return (
    <React.Fragment>
        <AppBar position="static" className={classes.appbar}>
        <Toolbar>
          <Typography className={classes.title} variant="h6" noWrap>
            Potato/Tomato Disease Classification
          </Typography>
        </Toolbar>
      </AppBar>
        <Container maxWidth={false} className={classes.mainContainer} disableGutters={true}>
        <div className={classes.content}>
            <Typography variant="h3" gutterBottom>
            Choose Prediction
            </Typography>
            <Button
            variant="contained"
            color="primary"
            className={classes.button}
            onClick={() => handleSelection('potato')}
            >
            Predict Potato
            </Button>
            <Button
            variant="contained"
            color="secondary"
            className={classes.button}
            onClick={() => handleSelection('tomato')}
            >
            Predict Tomato
            </Button>
        </div>
        </Container>
    </React.Fragment>
  );
};

export default SelectPrediction;